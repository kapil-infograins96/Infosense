from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

# Create your models here.

class Blog(models.Model):
    title = models.CharField(_("blogTitle"),max_length=500)
    description = models.TextField(_("blogDescription"),blank=True,null=True)
    content = models.TextField(_("blogContent"),blank=True,null=True)
    image = models.ImageField(_("blogImage"),upload_to="blog")
    slug = models.SlugField(_("blogSlug"),max_length=500,blank=True)
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)
    latest_blog = models.BooleanField(_("latest_blog"),default=False)

    class Meta:
        verbose_name_plural = "Blog"
    
    def __str__(self):
        return "{}".format(self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.title


class BlogHerosection(models.Model):
    blog_title = models.CharField(_("blogTitle"),max_length=250)
    content = models.TextField(_("content"))
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)
    
    def __str__(self) :
        return self.blog_title
