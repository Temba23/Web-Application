from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from users.models import Profile


# def home(request):
#     context = {
#         "posts" : Post.objects.all()
#     }
#     return render(request, "blog/home.html", context=context)

def about(request):
    return render(request, "blog/about.html", {"title":"Blog - About"})


"""
    CLASS BASED VIEW
"""

class PostListView(ListView):
    model = Post
    template_name = "blog/home.html" #<app_name>/<name_of_the_template>.html
    context_object_name = "posts"
    ordering = ['-date_posted'] # newest to oldest
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html" #<app_name>/<name_of_the_template>.html
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
            user = get_object_or_404(User, username=self.kwargs.get('username'))
            return Post.objects.filter(author = user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class ProfileDetailView(DetailView):
    model = Profile

# By using loginrequiredmixin it helps us by blocking the non-logged in user to the login url
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content", "attachment1", "attachment2"]


    # To set the current logged in user as the post_author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

# UserPassesTestMixin is used so that the user who have created the post can only update the post not random users.
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content", "attchment1", "attachment2"]


    # To set the current logged in user as the post_author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # to restrict the random users to update the post 
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
