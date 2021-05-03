from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User, GFGData


class RegisterUserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    name = serializers.CharField(max_length=255, required=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'password', 'handle_verified', 'token',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.handle_verified = validated_data.get('handle_verified', instance.handle_verified)
        instance.save()
        return instance

    @staticmethod
    def get_token(user):
        token = RefreshToken.for_user(user)
        return str(token.access_token)


class LoginUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    name = serializers.CharField(max_length=255, read_only=True)
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'password', 'handle_verified', 'token',)
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        return user

    @staticmethod
    def get_token(user):
        token = RefreshToken.for_user(user)
        return str(token.access_token)


class GFGDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GFGData
        fields = '__all__'
        extra_kwargs: {'user': {'write_only': True}}
