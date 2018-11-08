from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# LoginRequiredMixin for login requrired and UserPassesTestMixin for make sure the user is one does the update to post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

posts = Post.objects.all()


def home(request):

    args = {"posts":posts}

    return render(request,'blog/home.html',args)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<view_type>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


""" 
    template_name = 'blog/post_detail.html' "<app>/<model>_<view_type>.html"  
    not required since its the default path and name
    #By Default
    # context_object_name = 'object'
    # thats why change post to object
"""


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']
    # template_name = "<model_name>_form.html" default
    #success_url = 'blog-home'

    def form_valid(self, form): # tells that the form belong to the user logged in
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']
    # will use same template as create post 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request,'blog/about.html')


