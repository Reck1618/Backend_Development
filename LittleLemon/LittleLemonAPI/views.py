from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST'])
def books(request):
    if request.method == 'GET':
        return Response('list of the books', status=status.HTTP_200_OK)
    else:
        return Response('take the shit', status=status.HTTP_200_OK) 