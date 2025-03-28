from django.db import models
from users.models import Users

class Product(models.Model):
    # product_id = models.AutoField()      #### Unnecessary because Django adds `id` automatically
    name = models.CharField(max_length=100)
    story = models.CharField(max_length=800)
    price = models.FloatField()
    quantity = models.IntegerField()
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE, related_name='product')