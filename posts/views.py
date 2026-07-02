from django.shortcuts import render

from posts.models import Post


def home(request):
    post = {
        "title": "Welcome",
        "content": "This is your Django blog.",
        "image": "",
        "rate": "",
    }
    return render(request, "index.html", {"post": post})


def about(request):
    post = {
        "title": "About",
        "content": "This page is working.",
        "image": "",
        "rate": "",
    }
    return render(request, "index.html", {"post": post})


def post_list(request):
    q = request.GET.get("q", None)
    posts = Post.objects.filter(is_published=True)

    if q:
        posts = posts.filter(title__icontains=q)

    return render(
        request,
        "posts/post_list.html",
        {"posts": posts, "count": posts.count(), "request": request},
    )

def post_is_published(request):
    posts = Post.objects.filter(is_published=True)
    return render(
        request,
        "posts/post_list.html",
        {"posts": posts, "count": posts.count(), "request": request},
    )