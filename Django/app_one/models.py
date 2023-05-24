from django.db import models

# Create your models here.
class Menu(models.Model):
    dish_name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name + ':' + self.cuisine + ':' + str(self.price)
    

class Logger(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    time_logged = models.DateTimeField(auto_now_add=True)
