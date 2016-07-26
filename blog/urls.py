"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from posts.views import post_list, post_detail, user_detail, post_create, comment_create, like, post_update, random_users
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', post_list),
    url(r'^admin/', admin.site.urls),
    url(r'^post(?P<id>\d+)/$', post_detail, name="post_detail"),
    url(r'^user(?P<id>\d+)/$', user_detail),
    url(r'^create/$', post_create),
    url(r'^post(?P<id>\d+)/comment_create', comment_create),
    url(r'^post(?P<id>\d+)/like/$', like, name='like'),
    url(r'^post(?P<id>\d+)/edit/$', post_update, name='update'),
    url(r'^random_users/$', random_users),
    url(r'', include('registration.backends.simple.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)