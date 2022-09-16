from django.urls import path
from .views import (
    BlogAPI,
    SingleBlogAPI,
    LatestBlogAPI
)

urlpatterns = [
    path('blog_list/',BlogAPI.as_view()),
    path('<slug:blog_url>/',SingleBlogAPI.as_view(),name='blog'),
    path('latest_blog/',LatestBlogAPI.as_view(),name='latest-blog')
]