from django.db import models
# from django.contrib.auth.models import AbstractUser,Group,Permission

class Users(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=500)
    password = models.CharField(max_length=200)
    role = models.CharField(
        choices=(
            ('Admin' , 'Admin') , 
            ('Artist', 'Artist') , 
            ('Client', 'Client')
        ),
        max_length=10
    )

