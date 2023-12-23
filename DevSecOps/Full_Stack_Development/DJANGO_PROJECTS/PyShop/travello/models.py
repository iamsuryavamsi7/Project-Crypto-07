from django.db import models


class Destination(models.Model):
    place = models.CharField(max_length=20)
    desc = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField(upload_to="Destination_Pics")
    offer = models.BooleanField()

