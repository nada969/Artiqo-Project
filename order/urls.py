from django.urls import path
from . import views

urlpatterns =[
    path('neworderart/',views.neworderart,name='neworderart')
]

