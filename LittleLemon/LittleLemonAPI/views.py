from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import PlayerInfo, Team
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, throttle_classes, permission_classes
from rest_framework.views import APIView
from .serializers import PlayerInfoSerializer, TeamSerializer
from django.core.paginator import Paginator
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttles import TenCallsPerMinute
from rest_framework import viewsets

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
@api_view(['GET','POST'])
def players(request):

    if request.method == 'GET':
        players = PlayerInfo.objects.select_related('team').all()
        team_city = request.query_params.get('team')
        player_age = request.query_params.get('age')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')
        perpage = request.query_params.get('perpage', default=2)
        page = request.query_params.get('page', default=1)

        if team_city:
            players = players.filter(team__city=team_city) # try : ?team=delhi

        if player_age:
            players = players.filter(age__lte=player_age) # try : ?age=23

        if search:
            players = players.filter(name__istartswith=search) # try : ?search=b

        if ordering:
            ordering = ordering.split(',')
            players = players.order_by(*ordering) # try : ?ordering=-age

        paginator = Paginator(players, per_page=perpage)
        try:
            players = paginator.page(page)
        except:
            players = []

        serialized_info = PlayerInfoSerializer(players, many=True)
        return Response(serialized_info.data)

    if request.method == 'POST':
        serialized_item = PlayerInfoSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)

@api_view()
def single_player(request, id):
    player = get_object_or_404(PlayerInfo, pk=id)
    serialized_info = PlayerInfoSerializer(player)
    return Response(serialized_info.data)


@api_view()
def single_team(request, id):
    team = get_object_or_404(Team, pk=id)
    serialized_team = TeamSerializer(team)
    return Response(serialized_team.data)


@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message":"Bruce wayne is Batman"}, status.HTTP_200_OK)


@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name='Manager').exists():
        return Response({"message":"Only Managers should see this."}, status.HTTP_200_OK)
    else:
        return Response({"message":"You are not authorized to see this."}, status.HTTP_401_UNAUTHORIZED)


@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response({"message":"Successful"}, status.HTTP_200_OK)

@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([UserRateThrottle])
def throttle_check_auth(request):
    return Response({"message":"Successful"}, status.HTTP_200_OK)


@api_view()
@throttle_classes([TenCallsPerMinute])
def throttle_check_custom(request):
    return Response({"message":"Successful"}, status.HTTP_200_OK)


class PlayersViewSet(viewsets.ModelViewSet):
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = PlayerInfo.objects.all()
    serializer_class = PlayerInfoSerializer

    # custom throttle for different actions
    def get_throttles(self):
        if self.action == 'create':
            return [AnonRateThrottle]
        else:
            throttle_classes = [TenCallsPerMinute]
            return [throttle() for throttle in throttle_classes]

