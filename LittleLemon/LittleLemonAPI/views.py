from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import PlayerInfo
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import PlayerInfoSerializer

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


# Using Serializers
@api_view()
def players(request):
    players = PlayerInfo.objects.select_related('team').all()
    serialized_info = PlayerInfoSerializer(players, many=True)
    return Response(serialized_info.data)

@api_view()
def single_player(request, id):
    player = get_object_or_404(PlayerInfo, pk=id)
    serialized_info = PlayerInfoSerializer(player)
    return Response(serialized_info.data)
