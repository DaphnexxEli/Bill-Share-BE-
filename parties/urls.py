from django.urls import path, include
from .views import MemberViewSet, PartyViewSet

urlpatterns = [
    path('partyset', PartyViewSet.as_view()),
    path('memberset', MemberViewSet.as_view()),
   
]
