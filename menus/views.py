from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Restaurant, MenuItem
from .serializers import RestaurantSerializer, MenuItemSerializer
from rest_framework.permissions import IsAuthenticated

class RestaurantViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
