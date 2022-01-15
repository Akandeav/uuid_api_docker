import json, pytz
import requests, uuid, datetime
from .models import UUIDValue
from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import render
from .serializers import UUIDSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class UUIDView(APIView):
    """
    Randomly generates UUID
    Returns key-pair value of generated UUID

    key: timestamp
    value: UUID
    """

    def get(self, request):
        lagos = pytz.timezone('Africa/Lagos')
        time_stamp = datetime.datetime.now(tz=lagos).replace(tzinfo=None).isoformat(sep=" ")
        uuid_value = uuid.uuid4().hex
        data = {
            "time_stamp": time_stamp,
            "uuid": uuid_value
        }
        serializer = UUIDSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        all_uuid = UUIDValue.objects.all().values("time_stamp", "uuid").order_by('-time_stamp')
        out = {}
        for i in all_uuid:
            out[i['time_stamp']] = i['uuid']
        return JsonResponse(out, json_dumps_params={"indent":4})