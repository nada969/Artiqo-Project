from django.db import models
from users.models import Users

# Create your models here.
class Order(models.Model):
    order_id = models.IntegerField()
    total_price = models.FloatField()
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE, related_name='order')