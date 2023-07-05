from typing import Any, Optional
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Posts
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.
# user=User.objects.create_user(username='Honey',email='honey@gmail.com',password='12345')
# user.save()
# use=User.objects.filter(username='Honey').first()
# post1=Posts(title='Blog 2',content='Second post content',author_id=use.pk)
# post1.save()
posts=Posts.objects.all()

def home(request):
    return render(request,'home.html',{'posts':posts})

class PostListView(ListView):
    model=Posts
    template_name='home.html'
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by=2

class UserPostListView(ListView):
    model=Posts
    template_name='user.html'
    context_object_name='posts'
    
    paginate_by=2
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        
        return Posts.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model=Posts
    template_name='detail.html'

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Posts
    fields=['title','content']
    template_name='form.html'
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author=self.request.user
        return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Posts
    fields=['title','content']
    template_name='form.html'
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
class PostDeleteView(DeleteView):
    model=Posts
    template_name='delete.html'
    success_url='/'
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
        
def abt(request):
    return render(request,'about.html',{'title':'about'})