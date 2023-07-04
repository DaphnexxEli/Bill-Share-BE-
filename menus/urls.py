from django.urls import path, include
from .views import RestaurantViewSet, MenuItemViewSet

urlpatterns = [
    path('restaurantset', RestaurantViewSet.as_view()),
    path('menuset', MenuItemViewSet.as_view()),
   
]
