from django.urls import path
from . import views
from .views import OrderArtListCreateAPIView

urlpatterns =[
    path('neworderart/',views.place_order,name='neworderart'),
    path('orderartview/',views.OrderArtListCreateAPIView.as_view())
]

