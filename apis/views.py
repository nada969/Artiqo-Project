from rest_framework import generics , status
from users.models import Users
from users.serializers import UserSerializer  
from product.models import Product
from product.serializers import ProductSerializer
from order.models import OrderArt
from order.serializers import OrderArtSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from rest_framework.authtoken.models import Token
# from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate 
from django.contrib.auth import get_user_model

User = get_user_model()  # Gets your Users model

# @api_view(['GET','POST'])
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer



@api_view(['POST'])
def RegisterAPI(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.is_active = True  # Add this line
        user.save()
        # Debug: Check which table the user was saved to
        print(f"User saved to table: {user._meta.db_table}")  # Should print: users_users
        print(f"User ID: {user.pk}")
        
        if not user.pk:
            return Response({'detail': 'User was not saved properly'}, status=500)

        token, created = Token.objects.get_or_create(user=user)        
        return Response({
            "user": serializer.data,
            "token": token.key,
            "user_id": user.pk  # Add this to confirm
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from django.contrib.auth.hashers import check_password

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({"error":"username and password are required"},status=status.HTTP_400_BAD_REQUEST)
       
        user = authenticate(request, username=username, password=password)
        if user :
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        
        return Response({"error":"Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def user_logout(request):
#     if request.method == 'POST':
#         try:
#             # Delete the user's token to logout
#             request.user.auth_token.delete()
#             return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class ProductArtListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderArtListCreateAPIView(generics.ListCreateAPIView):
    queryset = OrderArt.objects.all()
    serializer_class = OrderArtSerializer


