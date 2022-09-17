from django.contrib import admin
from .models import (
    Blog,
    BlogHeroSection,
    MetaTag,
    BlogPageMetaTag
)
from django.utils.html import format_html

# Register your models here.
class BlogPageMetaTagAdmin(admin.ModelAdmin):
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')

    list_display  = ['title','content','admin_created_at','admin_updated_at']


class MetaTagAdmin(admin.ModelAdmin):
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')

    list_display  = ['blog','content','admin_created_at','admin_updated_at']

class BlogAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')
    
    list_display  = ['title','admin_created_at','admin_updated_at','latest']

class BlogHeroSectionAdmin(admin.ModelAdmin):
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')
    
    list_display  = ['title','content','admin_created_at','admin_updated_at']



admin.site.register(BlogHeroSection,BlogHeroSectionAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(MetaTag,MetaTagAdmin)
admin.site.register(BlogPageMetaTag,BlogPageMetaTagAdmin)



