from django.urls import path
from . import views
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeletelView,
                    UserPostListView)


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeletelView.as_view(), name='post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about', views.about, name='blog-about'),
    path('template', views.template, name='blog-template'),
    path('IdeaCapture', views.idea_capture_form, name='IdeaCapture'),
    path('DocCapture', views.doc_capture, name='DocCapture')
]


# path('', views.home, name='blog-home'), # old one
# path('myabout', = the path to the page, in this case local/myabout

