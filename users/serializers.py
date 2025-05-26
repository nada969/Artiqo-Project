from rest_framework import serializers
# from .models import Users
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
User = get_user_model()  # This gets your custom Users model (users_users)

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User  # Uses your custom Users model (users_users table)
        fields = ['username', 'email', 'password']  # Add your custom fields

    def create(self, validated_data):
        # Use create_user method for proper password hashing
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

