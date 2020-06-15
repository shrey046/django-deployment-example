from django.db import models

# Create your models here.
class User(models.Model):
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Email_ID = models.EmailField(max_length=254,unique=True)

    
