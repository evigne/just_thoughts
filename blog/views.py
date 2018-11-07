from django.shortcuts import render
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)

posts = Post.objects.all()


def home(request):

    args = {"posts":posts}

    return render(request,'blog/home.html',args)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  #<app>/<model>_<view_type>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    # template_name = 'blog/post_detail.html' "<app>/<model>_<view_type>.html"  not required since its the default path and name
    #By Default
    # context_object_name = 'object'
    # thats why change post to object


class PostCreateView(CreateView):
    model = Post
    fields = ['title','content']
    #template_name = "<model_name>_form.html"



def about(request):
    return render(request,'blog/about.html')


