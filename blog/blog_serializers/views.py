from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import (
    Blog,
    BlogHeroSection,
    BlogPageMetaTag
)
from .serializers import (
    BlogSerializer,
    SingleBlogSerializer,
    BlogListSerializer,
    BlogHeroSectionSerializer,
    BlogPageMetaTagSerializer
)

from rest_framework import (
    generics,
    filters,
    status,
)
from django.forms import model_to_dict
from rest_framework.generics import ListAPIView
from rest_framework import pagination

class blogListingAPI(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = pagination.LimitOffsetPagination


class BlogAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            # get_blog_instance = Blog.objects.filter(latest=True).order_by('-created_at')
            get_blog_instance = Blog.objects.all()
            
            serializer = BlogSerializer(get_blog_instance,many=True)
            blog_list = list(Blog.objects.all().values_list("title",flat=True))
            # get_blog_meta_content = BlogPageMetaTag.objects.first()
            # block_content_serializer = BlogPageMetaTagSerializer(get_blog_meta_content)
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "blog_list":blog_list,
                # "metacontent":block_content_serializer.data,
                "response":serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

class SingleBlogAPI(APIView):
    def get(self, request, blog_url, *args, **kwargs):
        try:
            get_blog_instance = Blog.objects.get(slug=blog_url)
            serializer = SingleBlogSerializer(get_blog_instance)
            blog_list = BlogListSerializer(Blog.objects.exclude(slug=blog_url),many=True)
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "blog_list":blog_list.data,
                "response":serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)


class BlogSearchAPI(APIView):
     def get(self, request, *args, **kwargs):
        try:
            get_blog_query = request.GET.get("blog")
            get_blog_instance = Blog.objects.filter(title__icontains = get_blog_query)
            serializer = BlogSerializer(get_blog_instance,many=True)
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "response":serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

 

class BlogHeroSectionAPI(APIView):
    def get(self, request, *args, **kwargs ):
        try:
            get_data = BlogHeroSection.objects.first()
            json_data = BlogHeroSectionSerializer(get_data)
            context = {
            "status":status.HTTP_200_OK,
            "status":True,
            "response":json_data.data,
            }            
            return Response(context, status.HTTP_200_OK)  
        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
            }    
        return Response(context,status=status.HTTP_400_BAD_REQUEST)