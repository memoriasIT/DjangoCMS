from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	path('posts/', views.posts, name='posts'),
	path('about/', views.about, name='about'),
	path('tools/', views.tools, name='tools'),
	url(r'^details/(?P<id>\d+)/$', views.details, name = 'details'),
]