from django.db import models

# Create your models here.

class EntryForm(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()

    def __unicode__(self):
        return self.name