from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import AccessToken

from users.models import User
from .serializers import UserSerializer


# Create your views here.
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        access_token = request.META.get("HTTP_AUTHORIZATION", "").split(" ")[1]

        try:
            decoded_token = AccessToken(access_token)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)

        user = User.objects.get(id=decoded_token["user_id"])

        response = Response()
        response.set_cookie(key="userID", value=user.id, httponly=True)
        response.set_cookie(key="email", value=user.email, httponly=True)
        response.set_cookie(key="first_name", value=user.first_name, httponly=True)
        response.set_cookie(key="last_name", value=user.last_name, httponly=True)
        response.set_cookie(key="phone", value=user.phone, httponly=True)
        response.set_cookie(key="is_staff", value=user.is_staff, httponly=True)

        response.data = {
            "userID": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "phone": user.phone,
            "is_staff": user.is_staff,
        }
        return response


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response = Response()
        # response.delete_cookie("access")
        # response.delete_cookie("refresh")
        response.data = {
            'message': 'success'
        }
        return response

class ResetPasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        email = request.data.get('email', None)
        new_password = request.data.get('new_password', None)

        if not email or not new_password:
            return Response({'error': 'Email and new password are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
            user.set_password(new_password)
            user.save()
            return Response({'message': 'Password reset successful'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)