from django.db import models
from users.models import Users

# Create your models here.

class cart(models.Model):
    total_price = models.FloatField()
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE, related_name='cart')


class cart_item(models.Model):
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE,related_name='cart_item')