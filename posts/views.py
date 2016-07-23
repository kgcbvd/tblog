from django.contrib import messages
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from posts.models import Post, Comment
from django.contrib.auth.models import User
from .forms import PostForm, CommentForm
import json

def post_create(request):
    if not request.user.is_authenticated():
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.author_id = User.objects.get(username=request.user).id
        instance.save()
        messages.success(request, 'Успешно создан')
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Ошибка!")
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)

def comment_create(request, id):
    if not request.user.is_authenticated():
        raise Http404
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author_id = User.objects.get(username=request.user).id
            instance.post_id = id
            instance.save()
            return HttpResponseRedirect('/post'+id)
    else:
        form = CommentForm()
    return render(request, 'comment_detail.html', {'form': form})

def post_list(request):
    queryset_list = []
    if request.user.is_authenticated():
        queryset_list = Post.objects.all()
    """
    paginator = Paginator(queryset_list, 10)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)"""

    context = {
        "post_list": queryset_list
    }
    return render(request, "post_list.html", context)

def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    if not request.user.is_authenticated():
        raise Http404
    username = User.objects.get(id=instance.author_id)
    comments = Comment.objects.filter(post_id=id)
    video = ''
    if instance.video:
        video = "https://www.youtube.com/embed/" + instance.video.split('v=')[-1]
    context = {"title": instance.title, "post_detail": instance, "author_info": username, "comments": comments,
               "video": video}
    return render(request, "post_detail.html", context)

def user_detail(request, id=None):
    user = get_object_or_404(User, id=id)
    posts = Post.objects.filter(author_id=id)
    context = {"user": user, "posts": posts}
    return render(request, "user.html", context)