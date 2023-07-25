from django.urls import path, include
from .views import MemberViewSet, PartyViewSet, Joinparty, CreateParty
from django.urls import path

urlpatterns = [
    path('partyset', PartyViewSet.as_view({"__all__"})),
    path('memberset', MemberViewSet.as_view({"__all__"})),
    path('joinParty', Joinparty.as_view()), 
    path('createParty', CreateParty.as_view())
]
