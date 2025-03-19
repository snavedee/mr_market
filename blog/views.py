from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    return render(request, 'mr_makeit/home.html')


def post_list(request):
    posts = Post.objects.all().order_by('-pub_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})