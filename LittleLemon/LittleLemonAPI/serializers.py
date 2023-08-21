from rest_framework import serializers
from .models import PlayerInfo, Team
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
import bleach

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
    player_name = serializers.CharField(source='name', max_length=255, validators=[UniqueValidator(queryset=PlayerInfo.objects.all())])
    yearly_salary = serializers.SerializerMethodField(method_name='salary')
    team = TeamSerializer(read_only=True)
    team_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = PlayerInfo
        fields = ('id', 'player_name', 'player_age', 'yearly_salary', 'team_id', 'team')
        validators = [
            UniqueTogetherValidator(
                queryset=PlayerInfo.objects.all(),
                fields=['player_name', 'player_age']
            )
        ]
        # depth = 1


    def salary(self, player: PlayerInfo):
        return (100 - player.age) * 1000

    # data validation
    def validate(self, attrs):
        attrs['name'] = bleach.clean(attrs['name'])
        if (attrs['age']<18):
            raise serializers.ValidationError('You are too young to play')
        if(attrs['age']>100):
            raise serializers.ValidationError('You are too old to play')
        return super().validate(attrs)