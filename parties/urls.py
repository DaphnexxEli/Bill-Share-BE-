from django.urls import path
from . import views

urlpatterns = [
    path('partyset', views.PartyViewSet.as_view({"__all__"})),
    path('memberset', views.MemberViewSet.as_view({"__all__"})),
    path('party/<str:code>/', views.getPartyByCode.as_view()),
    path('memberlist/<int:party_id>/', views.MemberListView.as_view()),
    path('history/<int:user_id>', views.getPartyByUserIdView.as_view()),
]
