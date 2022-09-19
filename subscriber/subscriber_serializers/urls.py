from django.urls import path
from .views import (
  SubscriberApi
)

urlpatterns = [

    path('subscriberdata/',SubscriberApi.as_view(),name='subscriber-data'),
    
]