from django.shortcuts import render
from suggester.models import SuggestedWord
from django.http import JsonResponse

# Create your views here.
from rest_framework import viewsets
from .models import Party, Member
from .serializers import PartySerializer, MemberSerializer, suggest_words

class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class suggest_words(request):
    query = request.GET.get('query', '')
    suggested_words = SuggestedWord.objects.filter(word__istartswith=query).values_list('word', flat=True)
    return JsonResponse(list(suggested_words), safe=False)