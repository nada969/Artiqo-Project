from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission



class Users(AbstractUser):
    # username = models.CharField(max_length=100, default='anonymous')
    email = models.EmailField(max_length=250,unique=True)
    # password = models.CharField(max_length=200)
    role = models.CharField(
        choices=(
            ('Admin' , 'Admin') , 
            ('Artist', 'Artist') , 
            ('Client', 'Client')
        ),
        max_length=10
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] # or [] if you only require email

    def __str__(self):
        return self.email
