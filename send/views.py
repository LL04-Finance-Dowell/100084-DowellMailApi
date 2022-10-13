from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Mails
from .serializers import MailSerializer
from django.http import HttpResponse 


# Create your views here.


class MailsList(APIView):
    def get(self, request, format=None):
        all_mails = Mails.objects.all()
        serializers = MailSerializer(all_mails, many=True)
        return Response(serializers.data)