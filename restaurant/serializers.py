from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import menu, booking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = menu 
        fields = '__all__'
    
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking 
        fields = '__all__'