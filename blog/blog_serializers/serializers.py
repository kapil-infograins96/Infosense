import re
from rest_framework import serializers
from django.utils.text import Truncator
from blog.models import (
    Blog,
    # BlogHerosection
)


class BlogSerializer(serializers.ModelSerializer):
    blog_url = serializers.SerializerMethodField()
    class Meta:
        model = Blog
        fields = ['id','title','description','slug','blog_url']
    
    def get_blog_url(self,obj):
        print(obj)
        return obj.get_absolute_url()

    def to_representation(self, obj):
        instance = super(BlogSerializer, self).to_representation(obj)
        instance['description'] = Truncator( instance['description']).words(50)
        return instance

class SingleBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id','title','content']
        
        
class LatestBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
        
        
# class BlogHerosectionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BlogHerosection
#         fields = '__all__'

 
