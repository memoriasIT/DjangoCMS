from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
	context = {
		'title': 'INDEX',
	}

	return render(request, 'posts/index.html', context)

def about(request):
	context = {
		'title': 'AB0UT',
	}

	return render(request, 'posts/about.html', context)

def tools(request):
	context = {
		'title': 'T00LS',
	}

	return render(request, 'posts/tools.html', context)

def posts(request):
	# return HttpResponse('Posts')
	posts = Posts.objects.all()
	
	paginator = Paginator(posts, 10)
	page = request.GET.get('page')

	posts = paginator.get_page(page)

	context = {
		'title': 'LATESTS P0STS',
		'posts': posts,
	}

	return render(request, 'posts/posts.html', context)

def details(request, id):
	post = Posts.objects.get(id = id)
	context ={
		'post': post
	}

	return render(request, 'posts/details.html', context)