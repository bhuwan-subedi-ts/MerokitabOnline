from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    add_state = models.CharField(max_length=100)
    add_district = models.CharField(max_length=100)
    add_town = models.CharField(max_length=100)
    add_ward = models.CharField(max_length=2,null=True)
    prof= models.CharField(max_length=100)
    interest = models.CharField(max_length=100)
    email = models.EmailField(null=False,blank=False,primary_key=True)
    phone_regex = RegexValidator(regex=r'^+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    photo = models.ImageField(upload_to='media/users')
    password = models.TextField(null=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='media/products')
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