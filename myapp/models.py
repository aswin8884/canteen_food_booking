from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Login_table(AbstractUser):
    usertype=models.CharField(max_length=25)

class User_registration(models.Model):

    name=models.CharField(max_length=25,null=True)
    usertype=models.CharField(max_length=25,null=True)
    address=models.CharField(max_length=150,null=True)
    contact=models.CharField(max_length=25,null=True)
    email=models.EmailField(null=True)
    profile_picture=models.ImageField(null=True)
    id_card=models.FileField(null=True)
    login_id=models.ForeignKey(Login_table,on_delete=models.CASCADE,null=True)

class Staff_registration(models.Model):

    name=models.CharField(max_length=25,null=True)
    address=models.CharField(max_length=150,null=True)
    contact=models.CharField(max_length=25,null=True)
    email=models.EmailField(null=True)
    profile_picture=models.ImageField(null=True)
    id_card=models.FileField(null=True)
    approvel=models.BooleanField(default=False)
    login_id=models.ForeignKey(Login_table,on_delete=models.CASCADE,null=True)