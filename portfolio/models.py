from django.db import models

# Create your models here.
class Product(models.Model):
    Name = models.CharField(max_length=200)
    Tagline = models.TextField(max_length=500)
