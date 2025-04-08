from django.urls import path
from . import views

urlpatterns =[
    path('neworderart/',views.place_order,name='neworderart'),
]

