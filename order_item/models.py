from django.db import models
from users.models import Users

# Create your models here.
class order_item(models.Model):
    order_item_id = models.IntegerField()
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE,related_name='order_item')