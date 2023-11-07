from django.urls import path
from . import views

urlpatterns = [
    path('restaurantset', views.RestaurantViewSet.as_view({"__all__"})),
    path('menuset', views.MenuItemViewSet.as_view({"__all__"})),
    path('menuitems/<int:restaurant_id>/', views.MenuItemListView.as_view()),
]
