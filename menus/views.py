# Create your views here.
from rest_framework import viewsets
from .models import Restaurant, MenuItem
from .serializers import RestaurantSerializer, MenuItemSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from menus.models import MenuItem

class RestaurantViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, restaurant_id, format=None):
        menuitems = MenuItem.objects.filter(restaurant=restaurant_id)
        serializer = MenuItemSerializer(menuitems, many=True)
        return Response(serializer.data)