from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
from parties.models import Party


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

class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        partyCode = request.COOKIES.get('code')

        try:
            decoded_token = AccessToken(access_token)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)

        party = Party.objects.get(id=decoded_token["user_id"])

        response = Response()
        response.set_cookie(key="email", value=user.email, httponly=True)
        response.set_cookie(key="first_name", value=user.first_name, httponly=True)
        response.set_cookie(key="last_name", value=user.last_name, httponly=True)
        response.set_cookie(key="phone", value=user.phone, httponly=True)
        response.set_cookie(key="is_staff", value=user.is_staff, httponly=True)

        response.data = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "phone": user.phone,
            "is_staff": user.is_staff,
        }
        return response

# class CreateParty(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         token = request.COOKIES.get('jwt')
#         if not token:
#             raise AuthenticationFailed('Unauthenticated!')
#         try:
#             payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated!')
#         user = users.objects.filter(id=payload['id']).first()
#         serializer = PartySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class Joinparty(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         token = request.COOKIES.get("jwt")
#         if not token:
#             raise AuthenticationFailed("Unauthenticated!")
#         try:
#             payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed("Unauthenticated!")
#         name = payload["first_name"]
#         cost = 0

#         party_id = request.data.get("party_id")
#         try:
#             party = Party.objects.get(id=party_id)
#         except Party.DoesNotExist:
#             return Response(
#                 {"message": "Invalid party"}, status=status.HTTP_400_BAD_REQUEST
#             )

#         # สร้างสมาชิกใหม่และบันทึกลงในฐานข้อมูล
#         member = Member.objects.create(party=party, name=name, cost=cost)
#         serializer = MemberSerializer(member)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
