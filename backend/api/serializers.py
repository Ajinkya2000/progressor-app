from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User, GFGData, LeetcodeData, DailyGFGData, DailyLeetcodeData


class RegisterUserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255, required=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'password', 'handle_verified', 'is_gfg',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.handle_verified = validated_data.get('handle_verified', instance.handle_verified)
        instance.is_gfg = validated_data.get('is_gfg', instance.is_gfg)
        instance.save()
        return instance


class LoginUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    name = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'password', 'handle_verified', 'is_gfg',)
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


class GFGDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GFGData
        fields = '__all__'
        extra_kwargs: {'user': {'write_only': True}}


class LeetcodeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeetcodeData
        fields = '__all__'
        extra_kwargs: {'user': {'write_only': True}}


class DailyGFGDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyGFGData
        fields = '__all__'


class DailyLeetcodeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLeetcodeData
        fields = '__all__'
