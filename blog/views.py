from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post, Category, Author


def home(request):
    # load all the posts from db(10)
    posts = Post.objects.all()[:11]
    cats = Category.objects.all()
    authors = Author.objects.all()
    data = {
        'posts': posts,
        'cats': cats,
        'authors': authors,
    }
    return render(request, 'home.html', data)


# Create your views here.
def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    author = Author.objects.all()
    return render(request, 'posts.html', {'post': post, 'cats': cats,'author':author})

def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, "category.html", {'cat': cat, 'posts': posts})


def author(request, url):
    auth = Author.objects.get(url=url)
    posts = Post.objects.filter(author=auth)
    # Render the template with author and posts data
    return render(request, "author.html", {'author': auth, 'posts': posts,})
