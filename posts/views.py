from django.contrib import messages
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from posts.models import Post, Comment, Like
from django.contrib.auth.models import User
from .forms import PostForm, CommentForm
import random
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

def post_update(request, id=None):
    if not request.user.is_authenticated() or User.objects.get(username=request.user).id != Post.objects.get(id=id).author_id:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "post_form.html", context)

def comment_create(request, id):
    if not request.user.is_authenticated():
        raise Http404
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author_id = User.objects.get(username=request.user).id
            instance.post_id = post.id
            instance.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = CommentForm()
    return render(request, 'comment_detail.html', {'form': form})

def post_list(request):
    queryset_list = []
    if request.user.is_authenticated():
        queryset_list = Post.objects.all()

    paginator = Paginator(queryset_list, 5)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "post_list": queryset
    }
    return render(request, "post_list.html", context)

def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    if not request.user.is_authenticated():
        raise Http404
    username = User.objects.get(id=instance.author_id)
    comments = Comment.objects.filter(post_id=id)
    try:
        rating = Like.objects.get(post_id=id).total_likes
    except:
        rating = 0
    liked = True
    try:
        user_liked = Like.objects.get(post_id=id, user=request.user)
    except:
        user_liked = None
    if not user_liked:
        liked = False
    video = ''
    if instance.video:
        video = "https://www.youtube.com/embed/" + instance.video.split('v=')[-1]
    updated = False
    if str(instance.created).split(".")[0] != str(instance.updated).split(".")[0]:
        updated = True
    may_updated = True
    if User.objects.get(username=request.user).id != Post.objects.get(id=id).author_id:
        may_updated = False
    context = {"title": instance.title, "post_detail": instance, "author_info": username, "comments": comments,
               "video": video, "rating": rating, "liked": liked, "updated": updated, "may_updated": may_updated}
    return render(request, "post_detail.html", context)

def user_detail(request, id=None):
    user = get_object_or_404(User, id=id)
    posts = Post.objects.filter(author_id=id)
    context = {"user": user, "posts": posts}
    return render(request, "user.html", context)

@csrf_exempt
def like(request, id):
    if not request.user.is_authenticated():
        raise Http404
    total_likes = 0
    if request.method == 'POST':
        user = request.user
        post = get_object_or_404(Post, id=id)
        try:
            liked = Like.objects.get(post_id=post.id)
        except:
            liked = Like.objects.create(post_id=post.id)
        try:
            user_liked = Like.objects.get(post_id=post.id, user=user)
        except:
            user_liked = None
        if not user_liked:
            liked.user.add(request.user)
            liked.total_likes += 1
            total_likes = liked.total_likes
            liked.save()
    return HttpResponse(total_likes)

def random_users(request):
    users_list = User.objects.all()
    users = {user.id: user.username for user in users_list}
    i = 0
    user_dict = {}
    while i < 5:
        el = random.choice(list(users.keys()))
        user_dict[el] = users[el]
        del users[el]
        i += 1
    return HttpResponse(json.dumps(user_dict), content_type="application/json")