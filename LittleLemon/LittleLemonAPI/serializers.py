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
    yearly_salary = serializers.SerializerMethodField(method_name='salary')
    team = TeamSerializer()

    class Meta:
        model = PlayerInfo
        fields = ('id', 'player_name', 'player_age', 'yearly_salary', 'team')

    def salary(self, player: PlayerInfo):
        return (100 - player.age) * 1000