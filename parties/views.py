from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from parties.models import Party
from django.shortcuts import get_object_or_404


# Create your views here.
from rest_framework import viewsets

from users.models import User
from .models import Party, Member
from .serializers import HistorySerializer, PartySerializer, MemberSerializer, MemberlistSerializer


class PartyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Party.objects.all()
    serializer_class = PartySerializer

    @action(detail=True, methods=["patch"])
    def update_order_list(self, request, pk=None):
        party = self.get_object()
        order_list = request.data.get("orderList")
        party.orderList = order_list
        party.save()
        return Response({"status": "Order list updated successfully"})


class MemberViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    @action(detail=True, methods=["patch"])
    def update_cost(self, request, pk=None):
        member = self.get_object()
        cost = request.data.get("cost")
        member.cost = cost
        member.save()
        return Response({"status": "Cost updated successfully"})


class getPartyByCode(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, code, format=None):
        try:
            party = Party.objects.get(Code=code)
            serializer = PartySerializer(party)
            return Response(serializer.data)
        except Party.DoesNotExist:
            return Response(
                {"error": "Party not found"}, status=status.HTTP_404_NOT_FOUND
            )


class MemberListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, party_id, format=None):
        members = Member.objects.filter(party=party_id).select_related('userID')
        serializer = MemberlistSerializer(members, many=True)
        return Response(serializer.data)


class getPartyByUserIdView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, user_id, format=None):
        members = Member.objects.filter(userID_id=user_id)
        serializer = HistorySerializer(members, many=True)
        return Response(serializer.data)
