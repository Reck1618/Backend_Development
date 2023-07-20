from rest_framework import serializers
from .models import PlayerInfo, Team

# class PlayerInfoSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField(max_length=255)
#     age = serializers.IntegerField()

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name', 'city')

class PlayerInfoSerializer(serializers.ModelSerializer):
    player_age  = serializers.IntegerField(source='age')
    player_name = serializers.CharField(source='name')
    ramaning_years = serializers.SerializerMethodField(method_name='remaning_years')
    team = TeamSerializer()

    class Meta:
        model = PlayerInfo
        fields = ('id', 'player_name', 'player_age', 'ramaning_years', 'team')

    def remaning_years(self, product: PlayerInfo):
        return 60 - product.age