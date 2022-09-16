from django.urls import path
from .views import (
    CountryDailingCodeAPI,
    ContactUsAPI
)

urlpatterns = [

    path('get_country_dialing_code/',CountryDailingCodeAPI.as_view(),name='get-country-dialing-code'),
    path('contact_us/',ContactUsAPI.as_view(),name='contact-us')

]