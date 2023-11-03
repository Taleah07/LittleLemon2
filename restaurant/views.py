from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import menu , booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import generics 
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

# Create your views here.
def index(request):
     return render(request, 'index.html', {})

class MenuView(generics.ListCreateAPIView):
     queryset = menu.objects.all()
     serializer_class = MenuSerializer

class MenuItemsView(generics.ListCreateAPIView):
     queryset = menu.objects.all()
     serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
     queryset = menu.objects.all()
     serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
   permission_classes = [IsAuthenticated]
   queryset = booking.objects.all()
   serializer_class = BookingSerializer