from django.shortcuts import render
from .models import Post

posts = Post.objects.all()

def home(request):

    args = {"posts":posts}

    return render(request,'blog/home.html',args)

def about(request):
    return render(request,'blog/about.html')
