from django.contrib import admin
from .models import Blog, BlogHerosection


# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')
    

    list_display  = ['title','admin_created_at','admin_updated_at']
    
# class BlogHerosectionAdmin(admin.ModelAdmin):
#     @admin.display(description='CreationDate')
#     def admin_created_at(self, obj):
#         return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
#     @admin.display(description='UpdatedDate')
#     def admin_updated_at(self, obj):
#         return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')
    

#     list_display  = ['title','admin_created_at','admin_updated_at']
# admin.site.register(BlogHerosection,BlogHerosectionAdmin)

admin.site.register(Blog,BlogAdmin)


