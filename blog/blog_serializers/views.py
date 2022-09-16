from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from blog.models import (
    Blog,
    
)
from .serializers import (
    BlogSerializer,
    SingleBlogSerializer,
    LatestBlogSerializer
)


class BlogAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_blog_instance = Blog.objects.all().order_by('created_at')[:4]
            serializer = BlogSerializer(get_blog_instance,many=True)
            blog_list = list(Blog.objects.all().values_list("title",flat=True))
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "blog_list":blog_list,
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
            blog_list = list(Blog.objects.exclude(slug=blog_url).values_list("title",flat=True))
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "blog_list":blog_list,
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
        

class LatestBlogAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
           
            
            blog_list = Blog.objects.filter(latest_blog = True)
                
            serializer = LatestBlogSerializer(blog_list)
            # blog_list = list(Blog.objects.all().values_list("title",flat=True))
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "blog_list":blog_list,
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
        
        
        
# class sectionApi(APIView):
#     def get(self, request, *args, **kwargs ):
#         try:
#             get_data = BlogHerosection.objects.all()
#             json_data = BlogHerosectionSerializer(get_data)
#             context = {
#             "status":status.HTTP_200_OK,
#             "status":True,
#             "response":json_data.data,
#             }            
            
#             return Response(context, status.HTTP_200_OK)  

#         except Exception as exception:
            
#             context = {
#                 "status":status.HTTP_400_BAD_REQUEST,
#                 "success":False,
#                 "response":str(exception)
                
#             }    
        
#         return Response(context,status=status.HTTP_400_BAD_REQUEST)