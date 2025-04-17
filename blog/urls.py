# Import the path function to define URL patterns
from django.urls import path

# Import views from the current app (to connect URLs to view functions)
from . import views

# Define the URL patterns for the blog app
urlpatterns = [
    # URL pattern for the homepage, which shows the list of blogs
    # '' means the root URL (e.g., http://localhost:8000/)
    path('', views.blog_list, name='blog_list'),

    # URL pattern for viewing details of a specific blog post
    # <int:pk> captures the blog post's primary key as an integer
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
]
