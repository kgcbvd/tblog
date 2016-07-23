from django.contrib import admin
from posts.models import Post, Comment, Like


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author_id', 'created', 'updated']
    class Meta:
        model = Post

class CommentAdmin(admin.ModelAdmin):
    list_display = ["post_id", "text", "created_on", "author_id"]
    class Meta:
        model = Comment

class LikeAdmin(admin.ModelAdmin):
    list_display = ["id", "post_id", "date", "total_likes"]
    class Meta:
        model = Like

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)