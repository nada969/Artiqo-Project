from django.urls import path
from . import views
from .views import ProductArtListCreateAPIView

app_name = 'products'

urlpatterns =[
    path('<int:pk>/',views.detail,name='productdetails'),
    path('products/',views.ProductArtListCreateAPIView.as_view())
]