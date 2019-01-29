from django.shortcuts import render
from blog.models import Post, Comment
from blog.forms import PostForm, CommentsForm
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,
                                  ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
# Create your views here.

# about page
class Aboutview(TemplateView):
    template_name = 'about.html'

# home page
class PostListView(ListView):
    model = Post
    def get_queryset(self):
        # (lte) less than and equal to
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

# post detail view
class PostDetailView(DetailView):
    model = Post

# create page
class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

# update page
class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

# delete
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

# draft
class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post
    def get_queryset(self):
        # (lte) less than and equal to
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')
