from django.shortcuts import render
from typing import Any, Dict
from django.db.models.query import QuerySet
from django.views.generic import ListView
from django.views import View
from django.db.models import Q

from . models import Post, Tag

# Create your views here.
class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        tags = Tag.objects.all()
        context["tags"] = tags
        return context
    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        data = queryset [:3]
        return data
    

class AllPostView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

class SinglePostView(View):
    template_name = "blog/post-detail.html"
    model = Post

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
                "post": post,
                "post_tags": post.tags.all(),
            }
        return render(request, "blog/post-detail.html", context)


def search_view(request):
    query = request.GET.get('q')
    tag = request.GET.get('tag')
    results = []

    if tag:
        results = Post.objects.filter(Q(tags__pk=tag)).distinct()
    elif query:
        results = Post.objects.filter(Q(title__icontains=query)| Q(tags__caption__icontains=query)| Q(excerpt__icontains=query)).distinct()  # Basic search by title

    context = {
        'query': query,
        'results': results,
    }

    return render(request, 'blog/search.html', context)



class ProposalPageView(View):
    template_name = "blog/proposal.html"
    model = Post

    def get(self, request):
        return render(request, "blog/proposal.html")
    
class MusicPageView(View):
    template_name = "blog/music.html"
    model = Post

    def get(self, request):
        return render(request, "blog/music.html")