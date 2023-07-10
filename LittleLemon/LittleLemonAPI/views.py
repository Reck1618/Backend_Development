from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Function based views
@api_view(['GET','POST'])
def books(request):
    if request.method == 'GET':
        return Response('list of the books', status=status.HTTP_200_OK)
    else:
        return Response('take the shit', status=status.HTTP_200_OK) 
    
# Class based views
class BookList(APIView):
    def get(self, request):
        author = request.GET.get('author')
        if author:
            return Response({"message":"list of books by " + author}, status.HTTP_200_OK)
        return Response({"message":"list of books"}, status.HTTP_200_OK)
    
    def post(self, request):
        return Response({"message":request.data.get('title') + " fuck shit up"}, status.HTTP_201_CREATED)
    

class Book(APIView):
    def get(self, request, pk):
        return Response({"message":"single book with id " + str(pk)}, status.HTTP_200_OK)
    
    def post(self, request, pk):
        return Response({"message":request.data.get("title")}, status.HTTP_200_OK)