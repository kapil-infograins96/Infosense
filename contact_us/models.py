from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class ContactUS(models.Model):
    fullName = models.CharField(_("fullName"),max_length=250)
    email = models.EmailField(_("emailId"),max_length=250)
    contactNumber = models.CharField(_("contactNumber"),max_length=100)
    countryName = models.CharField(_("countryName"),max_length=100)
    projectDescription = models.TextField(_("projectDescription"),help_text="PROJECT DESCRIPTION",default="")
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)


    class Meta:
        verbose_name_plural = "Contact"
    

    def __str__(self):
        return "{}".format(self.fullName)

