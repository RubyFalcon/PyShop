from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=20)
    float = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

class Offer(models.mode):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    discoutn =models.FloatField()