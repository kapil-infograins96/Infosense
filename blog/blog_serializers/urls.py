from django.urls import path
from .views import (
    BlogAPI,
    SingleBlogAPI,
    BlogSearchAPI,
    blogListingAPI,
    BlogHeroSectionAPI
)

urlpatterns = [
    path('blog_list/',BlogAPI.as_view()),
    path('blog/blog_section_one/',BlogHeroSectionAPI.as_view(),name='blog-hero-section'),
    path('<slug:blog_url>/',SingleBlogAPI.as_view(),name='blog'),
    path("search_query/title/",BlogSearchAPI.as_view(),name='blog-search'),
    path('blog/blog-listing/',blogListingAPI.as_view(),name='blog-listing'),
]   