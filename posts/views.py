from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from posts.models import Post, Comment
from django.contrib.auth.models import User

def post_list(request):
    queryset_list = []
    if request.user.is_authenticated():
        queryset_list = Post.objects.all()

    paginator = Paginator(queryset_list, 10)
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
    context = {"title": instance.title, "post_detail": instance, "author_info": username}
    return render(request, "post_detail.html", context)

def user_detail(request, id=None):
    user = get_object_or_404(User, id=id)
    posts = Post.objects.filter(author_id=id)
    context = {"user": user, "posts": posts}
    return render(request, "user.html", context)