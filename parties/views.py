from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Party, Member
from .serializers import PartySerializer, MemberSerializer

class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer