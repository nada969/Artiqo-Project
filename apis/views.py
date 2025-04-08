from rest_framework import generics
from users.models import Users
from users.serializers import UserSerializer
from product.models import Product
from product.serializers import ProductSerializer
from order.models import OrderArt
from order.serializers import OrderArtSerializer


# Create your views here.

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

# from rest_framework.viewsets import ModelViewSet
# class UsersAPI(ModelViewSet):
#     queryset = Users.objects.all()
#     serializer_class = UserSerializer



class ProductArtListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderArtListCreateAPIView(generics.ListCreateAPIView):
    queryset = OrderArt.objects.all()
    serializer_class = OrderArtSerializer


