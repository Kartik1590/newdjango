from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView

urlpatterns=[
    path('',PostListView.as_view(),name='blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='blog-detail'),
    path('about/',views.abt,name='blog-abt'),
    path('post/new/',PostCreateView.as_view(),name='blog-create'),
    path('post/<int:pk>/update',PostUpdateView.as_view(),name='blog-update'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name='blog-delete'),
    path('user/<str:username>',UserPostListView.as_view(),name='blog-user-post'),
    
    

]

urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)