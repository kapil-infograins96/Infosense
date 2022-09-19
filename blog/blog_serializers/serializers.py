import re
from rest_framework import serializers
from django.utils.text import Truncator
from blog.models import (
    Blog,
    BlogHeroSection,
    MetaTag,
    BlogPageMetaTag
)

class BlogPageMetaTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPageMetaTag
        fields = ['title','content']

class BlogHeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogHeroSection
        fields = '__all__'


class BlogListSerializer(serializers.ModelSerializer):
    blog_url = serializers.SerializerMethodField()
    class Meta:
        model = Blog
        fields = ['title','blog_url']
    
    def get_blog_url(self,obj):
        return obj.get_absolute_url()

class BlogSerializer(serializers.ModelSerializer):
    blog_url = serializers.SerializerMethodField()
    class Meta:
        model = Blog
        fields = ['id','title','description','content','image','slug','blog_url']
    
    def get_blog_url(self,obj):
        return obj.get_absolute_url()

    def to_representation(self, obj):
        instance = super(BlogSerializer, self).to_representation(obj)
        instance['description'] = Truncator( instance['description']).words(30)
        return instance

class MetaTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaTag
        fields = ['title','content']

class SingleBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id','title','content','image']
    
    def to_representation(self, obj):
        instance = super(SingleBlogSerializer, self).to_representation(obj)
        try:
            instance['metacontent'] = MetaTagSerializer(MetaTag.objects.get(blog__slug=obj.slug)).data
        except Exception as exception:
            instance['metacontent'] = {}
        return instance



