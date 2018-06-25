from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path

urlpatterns = [
	path('', include('posts.urls')),
	url(r'^$', include('posts.urls')),
	url(r'^admin/', admin.site.urls),
    url(r'^posts/', include('posts.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
