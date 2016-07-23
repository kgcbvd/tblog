from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(upload_to='images', blank=True)
    video = models.URLField(blank=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    author = models.ForeignKey(User)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"id": self.id})

class Comment(models.Model):
    post = models.ForeignKey(Post)
    created_on = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=300)
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

class Like(models.Model):
    user = models.ManyToManyField(User, related_name='likes')
    post = models.ForeignKey(Post)
    date = models.DateTimeField(auto_now_add=True)
    total_likes = models.IntegerField(default=0)