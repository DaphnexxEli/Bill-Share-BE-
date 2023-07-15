from django.shortcuts import render

# from suggester.models import SuggestedWord
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from billshare.settings import SECRET_KEY
import jwt
import users

# Create your views here.
from rest_framework import viewsets
from .models import Party, Member
from .serializers import PartySerializer, MemberSerializer


class PartyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    queryset = Party.objects.all()
    serializer_class = PartySerializer


class MemberViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class CreateParty(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        user = users.objects.filter(id=payload['id']).first()
        serializer = PartySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Joinparty(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        token = request.COOKIES.get("jwt")
        if not token:
            raise AuthenticationFailed("Unauthenticated!")
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated!")
        name = payload["first_name"]
        cost = 0

        party_id = request.data.get("party_id")
        try:
            party = Party.objects.get(id=party_id)
        except Party.DoesNotExist:
            return Response(
                {"message": "Invalid party"}, status=status.HTTP_400_BAD_REQUEST
            )

        # สร้างสมาชิกใหม่และบันทึกลงในฐานข้อมูล
        member = Member.objects.create(party=party, name=name, cost=cost)
        serializer = MemberSerializer(member)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# class suggest_words(request):
#     query = request.GET.get('query', '')
#     suggested_words = SuggestedWord.objects.filter(word__istartswith=query).values_list('word', flat=True)
#     return JsonResponse(list(suggested_words), safe=False)
