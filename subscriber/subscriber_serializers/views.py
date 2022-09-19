import json
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from subscriber.models import (
    Subscriber
    
)


class SubscriberApi(APIView):
    def post(self, request, *args, **kwargs):
        try:
            get_subscriber = request.POST.get('get_subscriber')
            get_json = json.loads(get_subscriber)
            subs = Subscriber(
                subuser = get_json['emailid']
            )
            subs.save()
            context = {
                        "status":status.HTTP_201_CREATED,
                        "success":True,
                        "response":"Successfully Created!"
                    }

            return JsonResponse(context,status=status.HTTP_201_CREATED)

        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
            }
            return JsonResponse(context,status=status.HTTP_400_BAD_REQUEST)