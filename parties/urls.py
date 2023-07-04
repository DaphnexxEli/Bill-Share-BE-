from django.urls import path, include
from .views import MemberViewSet, PartyViewSet
from django.urls import path
# from suggester.views import suggest_words

urlpatterns = [
    path('partyset', PartyViewSet.as_view()),
    path('memberset', MemberViewSet.as_view()),
    # path('api/suggest-words/', suggest_words, name='suggest-words')
   
]
