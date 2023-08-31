from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts", views.AllPostView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(),
          name="post-detail-page"),
    path('search/', views.search_view, name='search_view'),
    path('proposal', views.ProposalPageView.as_view(), name="proposal"),
    path('music', views.MusicPageView.as_view(), name="music"),
    path('in-progress', views.InProgressPostView.as_view(), name="in-progress"),

        # /posts/my-first-post
    # path("read-later", views.ReadLaterView.as_view(), name="read-later")
]

