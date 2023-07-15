from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User
from .serializers import UserSerializer
import datetime
# import jwt
from billshare.settings import SECRET_KEY

# Create your views here.
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# class LoginView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         email = request.data['email']
#         password = request.data['password']

#         user = User.objects.filter(email=email).first()
#         user = au
#         if user is None:
#             raise AuthenticationFailed('User not found')
        
#         if not user.check_password(password):
#             raise AuthenticationFailed('Incorrect password!')

#         payload = {
#             'id': user.id,
#             'email': user.email,
#             'first_name': user.first_name,
#             'last_name': user.last_name,
#             'phone': user.phone,
#             'is_staff': user.is_staff,
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#             'iat': datetime.datetime.utcnow(),
#         }

#         token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

#         response = Response()
#         response.set_cookie(key='jwt', value=token, httponly=True)
#         response.set_cookie(key='email', value=user.email, httponly=True)
#         response.set_cookie(key='first_name', value=user.first_name, httponly=True)
#         response.set_cookie(key='last_name', value=user.last_name, httponly=True)
#         response.set_cookie(key='phone', value=user.phone, httponly=True)
#         response.set_cookie(key='is_staff', value=user.is_staff, httponly=True)
        
#         response.data = {
#             'jwt': token,
#             'first_name': user.first_name,
#             'last_name': user.last_name,
#             'email': user.email,
#             'phone': user.phone,
#             'is_staff' : user.is_staff
#         }
#         return response

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        response = Response()
        # response.delete_cookie('jwt')
        response.delete_cookie('token')
        response.delete_cookie('refresh_token')
        response.data = {
            'message': 'success'
        }
        return response

# class UserView(APIView):
#     def get(self, request):
#         token = request.COOKIES.get('jwt')
#         if not token:
#             raise AuthenticationFailed('Unauthenticated!')
#         try:
#             payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated!')

#         user = User.objects.filter(id=payload['id']).first()
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
        