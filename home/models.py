from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# Create your models here

class Product(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='media')
    details = models.TextField()
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.TextField(max_length=6)
    published_date = models.DateField()
    category = models.TextField(max_length=50)
    featured = models.BooleanField()

class admin(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    email = models.EmailField(null=False,blank=False)