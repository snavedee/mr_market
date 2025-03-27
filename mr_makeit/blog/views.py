from django.shortcuts import render, get_object_or_404
from django.utils.http import urlencode
from .models import Post

def home(request):
    return render(request, 'mr_makeit/home.html')

def post_list(request):
    posts = Post.objects.all().order_by('-pub_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post_url = request.build_absolute_uri()  # Get full URL of the post
    twitter_share_url = f"https://twitter.com/intent/tweet?{urlencode({'text': post.title, 'url': post_url})}"
    
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'post_url': post_url,
        'twitter_share_url': twitter_share_url,
    })
