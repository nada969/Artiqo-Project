from django.db import models
from users.models import Users

# Create your models here.
class cart_item(models.Model):
    cart_item_id = models.IntegerField()
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE,related_name='cart_item')