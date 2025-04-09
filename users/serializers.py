from rest_framework import serializers
from .models import Users
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Users(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Users
#         fields = ('id', 'name', 'email', 'password', 'role')

    