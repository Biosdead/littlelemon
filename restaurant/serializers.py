from rest_framework import serializers
from .models import menu,booking
from django.contrib.auth.models import User


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = '__all__'

class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
#MenuItemSerializer