import json
import pycountry
import phonenumbers
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from django.http import JsonResponse
from phone_iso3166.country import *
from contact_us.models import (
    ContactUS
)
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.html import strip_tags

class CountryDailingCodeAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            df_country = pd.read_csv('./contact_us/country_data/country.csv')
            df_country = df_country[df_country['Dial'].notna()]
            df_country['Dial'] = df_country['Dial'].apply(lambda x : x.replace("-",""))
            df_country.drop_duplicates(subset=['Dial'],inplace=True)
            df_country['Dial'] = df_country['Dial'].apply(lambda x : x.split(",")[0])
            df_country = df_country[['FIFA','Dial']]
            new_row = pd.DataFrame({'FIFA':'IND', 'Dial':'91'},index =[0])
            df_country = pd.concat([new_row, df_country]).reset_index(drop = True)
            df_country.drop_duplicates(subset=['Dial'],inplace=True)
            df_country['Dial'] = df_country['Dial'].apply(lambda x : "+" + x)
            df_country['country_with_dialing_code'] = df_country['FIFA'] + " " + df_country['Dial']
            df_country.dropna(inplace=True)
            df_country = df_country[['country_with_dialing_code','Dial']]
            country_list = list(df_country.to_dict('index').values())
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "response":{
                    "country_dialing_code":country_list
                }
            }
            return Response(context)
        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

class ContactUsAPI(APIView):
    def post(self, request, *args, **kwargs):
        try:
            flag = None
            get_contact_detail = request.POST.get('get_contact_detail')
            get_json = json.loads(get_contact_detail)
            get_contact_number = get_json['contactNumber']
            if get_contact_number != "":
                get_country_carrier = phone_country(get_json['dialingCode'])
                check_number = phonenumbers.parse(get_json['contactNumber'], get_country_carrier)
                flag = phonenumbers.is_valid_number(check_number)
                if flag:
                    get_country_name = pycountry.countries.get(alpha_2=phone_country(get_json['contactNumber']))
                    try:
                        get_ip = request.META.get('REMOTE_ADDR', None)
                        get_content = requests.get('http://ip-api.com/json/'+ "65.0.43.174")
                        #lets decode to ut8-8
                        get_content = get_content.content.decode('UTF-8')
                        get_content_as_dictionary = json.loads(get_content)
                    except Exception as exception:
                        pass
                    client_info = ContactUS(
                        fullName = get_json['fullName'],
                        email = get_json['emailId'],
                        contactNumber = get_json['contactNumber'],
                        countryName = get_country_name.name,
                        subject = get_json['subject'],
                        message = get_json['message'],
                        regionName = get_content_as_dictionary.get('regionName','Not Able to fetch region'),
                        city = get_content_as_dictionary.get('city','Not Able to fetch city'),
                    )
                    client_info.save()
                    context = {
                        "status":status.HTTP_201_CREATED,
                        "success":True,
                        "response":"Successfully Created!"
                    }
                    #for infograins client
                    subject = "Thanks for contacting infograins"
                    html_message = render_to_string('send_mail/send_mail_to_client.html',{"Name":get_json['fullName']})
                    plain_message = strip_tags(html_message)
                    from_email = 'kapilyadav@infograins.com'
                    to = get_json['emailId']
                    send_mail(subject, plain_message, from_email, [to], html_message=html_message,fail_silently=False)
                    #for infograins founder
                    subject = "Congratulation for new client"

                    content = {
                    "Name":client_info.fullName,
                    "Email":client_info.email,
                    "Subject":client_info.subject,
                    "Message":client_info.message,
                    "Location":client_info.regionName + client_info.city,
                    "MobileNumber":client_info.contactNumber,
                }
                    html_message = render_to_string('send_mail/send_mail_to_infograins.html',content)
                    plain_message = strip_tags(html_message)
                    from_email = 'kapilyadav@infograins.com'
                    to = "kapilyadav@infograins.com"
                    send_mail(subject, plain_message, from_email, [to], html_message=html_message,fail_silently=False)
                    return JsonResponse(context,status=status.HTTP_201_CREATED)
                else:
                    context = {
                        "status":status.HTTP_400_BAD_REQUEST,
                        "success":False,
                        "response":"Phone number is not valid!"
                    }
                    return JsonResponse(context,status=status.HTTP_400_BAD_REQUEST)
            else:
                try:
                    get_ip = request.META.get('REMOTE_ADDR', None)
                    get_content = requests.get('http://ip-api.com/json/'+ '65.0.43.174')
                    #lets decode to ut8-8
                    get_content = get_content.content.decode('UTF-8')
                    get_content_as_dictionary = json.loads(get_content)
                    print(get_content_as_dictionary)
                except Exception as exception:
                    pass
                client_info = ContactUS(
                    fullName = get_json['fullName'],
                    email = get_json['emailId'],
                    contactNumber = get_contact_number,
                    countryName = get_content_as_dictionary['country'],
                    subject = get_json['subject'],
                    message = get_json['message'],
                    regionName = get_content_as_dictionary.get('regionName',''),
                    city = get_content_as_dictionary.get('city',''),
                )
                client_info.save()
                context = {
                    "status":status.HTTP_201_CREATED,
                    "success":True,
                    "response":"Successfully Created!"
                }
                #for infograins client
                subject = "Thanks for contacting infograins"
                html_message = render_to_string('send_mail/send_mail_to_client.html',{"Name":get_json['fullName']})
                plain_message = strip_tags(html_message)
                from_email = 'kapilyadav@infograins.com'
                to = get_json['emailId']
                send_mail(subject, plain_message, from_email, [to], html_message=html_message,fail_silently=False)
                #for infograins founder
                subject = "Congratulation for new client"
                content = {
                    "Name":client_info.fullName,
                    "Email":client_info.email,
                    "Subject":client_info.subject,
                    "Message":client_info.message,
                    "Location":client_info.regionName + client_info.city,
                    "MobileNumber":None,
                }
                html_message = render_to_string('send_mail/send_mail_to_infograins.html',content)
                plain_message = strip_tags(html_message)
                from_email = 'kapilyadav@infograins.com'
                to = "kapilyadav@infograins.com"
                send_mail(subject, plain_message, from_email, [to], html_message=html_message,fail_silently=False)
                return JsonResponse(context,status=status.HTTP_201_CREATED)

        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
            }
            return JsonResponse(context,status=status.HTTP_400_BAD_REQUEST)