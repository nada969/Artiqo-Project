from django.contrib import admin
from .models import Order , order_item , OrderArt
# Register your models here.
admin.site.register(Order)
admin.site.register(order_item)
admin.site.register(OrderArt)