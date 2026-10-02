from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Profile


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    phone = serializers.CharField(write_only=True)
    address = serializers.CharField(write_only=True)
    city = serializers.CharField(write_only=True)
    country = serializers.CharField(write_only=True)

    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
            'confirm_password',
            'phone',
            'address',
            'city',
            'country',
        ]

    def validate(self, data):

        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({
                'confirm_password': 'Passwords do not match.'
            })

        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({
                'email': 'Email already exists.'
            })

        return data

    def create(self, validated_data):

        validated_data.pop('confirm_password')

        phone = validated_data.pop('phone')
        address = validated_data.pop('address')
        city = validated_data.pop('city')
        country = validated_data.pop('country')

        password = validated_data.pop('password')

        email = validated_data['email']

        user = User.objects.create_user(
            username=email,
            password=password,
            **validated_data
        )

        Profile.objects.create(
            user=user,
            phone=phone,
            address=address,
            city=city,
            country=country
        )

        return user

# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         token['email'] = user.email

#         return token

#     def validate(self, attrs):
#         data = super().validate(attrs)

#         data['user'] = {
#             'id': self.user.id,
#             'first_name': self.user.first_name,
#             'last_name': self.user.last_name,
#             'email': self.user.email,
#         }

#         return data


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        profile = getattr(self.user, 'profile', None)

        data['user'] = {
            'id': self.user.id,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'email': self.user.email,
            'phone': profile.phone if profile else '',
            'address': profile.address if profile else '',
        }

        return data

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = [
            'phone',
            'address',
        ]    