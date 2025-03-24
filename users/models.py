from django.db import models

class Users(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=500)
    password = models.CharField(max_length=200)
    role = models.CharField(
        choices=(
            (1 , 'Admin') , 
            (2, 'Artist') , 
            (3, 'Client')
        ),
        max_length=1
    )
