from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class  Usuario(AbstractUser):
    username =models.CharField(max_length=30, primary_key=True)
    full_name=models.CharField(max_length=150,null=False,blank=True )
    email= models.CharField(max_length=250, null=False)

    USERNAME_FIELD ="username"
    REQUIRED_FIELDS= ['full_name','email']

    class Meta:
        db_table="usuarios"




