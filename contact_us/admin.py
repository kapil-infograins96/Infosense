from django.contrib import admin
from django.utils.html import format_html
from .models import (
    ContactUS
)

# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')

    @admin.display(description='project_description')
    def display_projectDescription(self, obj):
        return format_html(
            '<textarea cols="60" rows="4" readonly>{}</textarea>',
            obj.projectDescription)

    list_display  = ['fullName','email','contactNumber','countryName','display_projectDescription','admin_created_at','admin_updated_at']

admin.site.register(ContactUS, ContactUsAdmin)