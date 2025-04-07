from django.shortcuts import render , get_object_or_404
from product.models import Product
from rest_framework import generics
from .serializers import ProductSerializer

# Create your views here.
def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request, 'product/productdetails.html', {'product': product})

class ProductArtListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
