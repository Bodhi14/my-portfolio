from email import message
from multiprocessing import context
from urllib.request import Request
from webbrowser import get
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from Portfolio import settings
from .serializers import InfoSerializer
from .models import Info
from rest_framework.parsers import JSONParser
from rest_framework import *
from rest_framework.status import *
from rest_framework.permissions import *
from rest_framework.decorators import APIView


def home(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        user = Info.objects.create()

        user.name = name
        user.email = email
        user.subject = subject
        user.message = message

        user.save()

        return render(request, 'app/index.html' ,context={'name':name,'subject':subject,'msg':message})

        

    return render(request, 'app/index.html')


class InfoAPI(APIView):

    def get(self, request, pk=None, format=None):
        if pk is not None:
            item = Info.objects.get(pk=pk)
            serializer = InfoSerializer(item)
            return Response(serializer.data)
            
        
        items = Info.objects.all()
        serializer = InfoSerializer(items, many=True)
        return Response(serializer.data)
        


        




    






