from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from parties.models import Party


# Create your views here.
from rest_framework import viewsets
from .models import Party, Member
from .serializers import PartySerializer, MemberSerializer


class PartyViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    
    queryset = Party.objects.all()
    serializer_class = PartySerializer


class MemberViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class getPartyByCode(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, code, format=None):
        try:
            party = Party.objects.get(Code=code)
            serializer = PartySerializer(party)
            return Response(serializer.data)
        except Party.DoesNotExist:
            return Response({"error": "Party not found"}, status=status.HTTP_404_NOT_FOUND)
