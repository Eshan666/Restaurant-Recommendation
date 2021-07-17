from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Burger(models.Model):
    name = models.CharField(max_length=50,null=True)
    price = models.CharField(max_length=40,null=True)
    rating = models.FloatField(max_length=10,null=True)

class Sandwich(models.Model):
    name = models.CharField(max_length=50,null=True)
    price = models.CharField(max_length=40,null=True)
    rating = models.FloatField(max_length=10,null=True)

class Pizza(models.Model):
    name = models.CharField(max_length=50,null=True)
    price = models.CharField(max_length=40,null=True)
    rating = models.FloatField(max_length=10,null=True)

class Biriyani(models.Model):
    name = models.CharField(max_length=50,null=True)
    price = models.CharField(max_length=40,null=True)
    rating = models.FloatField(max_length=10,null=True)

class Pasta(models.Model):
    name = models.CharField(max_length=50,null=True)
    price = models.CharField(max_length=40,null=True)
    rating = models.FloatField(max_length=10,null=True)