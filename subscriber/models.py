from django.db import models
from django.utils.translation import gettext_lazy as _


class Subscriber(models.Model):
    subuser = models.EmailField(_("emailId"),max_length=250)
    
    def __str__(self): 
        return "{}".format(self.subscriber)
    
    
    
    