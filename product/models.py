from django.db import models
from users.models import Users

class Product(models.Model):
    # product_id = models.AutoField()      #### Unnecessary because Django adds `id` automatically
    name = models.CharField(max_length=100, blank=True)
    story = models.TextField(blank=True,null=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    is_sold = models.BooleanField(default=False)
    image = models.ImageField(upload_to='product_images',blank=True, null=True)
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name 