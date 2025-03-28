from django.db import models
from users.models import Users

# Create your models here.
class Order(models.Model):
    total_price = models.FloatField()
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE, related_name='order')


class order_item(models.Model):
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE,related_name='order_item')