from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'id', 'token']

    def get_token(self, user):
        token = RefreshToken.for_user(user)
        return str(token.access_token)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginUserSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    name = serializers.CharField(max_length=255, read_only=True)
    token = serializers.SerializerMethodField(read_only=True)

    def get_token(self, user):
        token = RefreshToken.for_user(user)
        return str(token.access_token)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        return user


class GFGSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, required=True)

