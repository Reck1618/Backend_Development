from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class PlayerInfo(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.PROTECT, default=1)