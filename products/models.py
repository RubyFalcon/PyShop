from django.db import models
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

    def get_absolute_url(self):
        return reverse("products:product-detail",kwargs={"id": self.id})

class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()