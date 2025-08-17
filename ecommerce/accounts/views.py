from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


