from django.db import models


class Product(models.Model):
    place = models.CharField(max_length=20)
    desc = models.CharField(max_length=255)

