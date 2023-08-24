from django.contrib import admin
from . models import Post, Author, Tag, Comments

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "author", "date")
    list_filter = ("author", "date", "tags",)

class AuthorAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

class CommentsAdmin(admin.ModelAdmin):
    list_display = ("user_name", "text", "post",)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)