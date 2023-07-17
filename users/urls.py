from django.urls import path, include
from .views import RegisterView, LogoutView, UserView 

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('getuser', UserView.as_view()),
    path('logout', LogoutView.as_view()),
]
