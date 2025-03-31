from django.db import models
from django.conf import settings
from users.models import Users

# Create your models here.
class Order(models.Model):
    total_price = models.FloatField()
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE, related_name='order')


class order_item(models.Model):
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE,related_name='order_item')

class OrderArt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    artist_email = models.EmailField()
    art_name = models.CharField(max_length=200)
    story = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order by {self.user.username} for {self.art_name}"