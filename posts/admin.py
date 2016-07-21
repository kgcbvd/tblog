from django.contrib import admin
from posts.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author_id', 'created', 'updated', 'rating']
    class Meta:
        model = Post

class CommentAdmin(admin.ModelAdmin):
    list_display = ["post_id", "text", "created_on", "author_id"]
    class Meta:
        model = Comment

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)