from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    rating = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images')
    video = models.URLField()
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post)
    created_on = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=300)
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.title
