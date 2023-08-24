from django.db import models
from django.db.models.fields import DateField, SlugField
from ckeditor.fields import RichTextField

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self) -> str:
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=300)
    title_image = models.ImageField(upload_to="posts", null=True)
    post_image = models.ImageField(upload_to="posts", null=True)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)
    slug = models.SlugField(unique=True, db_index=True)
    content = RichTextField()
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, related_name="posts", null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self) -> str:
        return f"{self.title}"
    
class Comments(models.Model):
    user_name = models.CharField(max_length=150)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.text

    
