from django.db import models
# from django.contrib.auth.models import
# Create your models here.

class Cour(models.Model):
    titre = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.titre