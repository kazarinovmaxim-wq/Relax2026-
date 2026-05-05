from django.shortcuts import render
from .data import posts

def index(request):
    return render(request, 'blog/index.html', context={'posts': posts[::-1]})

def post_detail(request, id):
    post = next((post for post in posts if int(post['id']) == int(id)), None)
    if post is None:
        from django.http import Http404
        raise Http404("Пост не найден")
    return render(request, 'blog/detail.html', context={'post': post})

def category_posts(request, category_slug):
    category_posts = [post for post in posts if post['category'] == category_slug]
    return render(request, 'blog/category.html', context={'posts': category_posts, 'category_slug': category_slug})