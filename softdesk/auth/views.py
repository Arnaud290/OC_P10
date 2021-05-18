"""Logins views and account creation module"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from auth import serializers


class SignupView(generics.CreateAPIView):
    """
    User account creation view class.
    Access authorized to everyon
    """
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = serializers.RegisterSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    """
    Token recovery view class.
    Access to people with the correct password
    """
    permission_classes = [AllowAny]
    serializer_class = serializers.MyTokenObtainPairSerializer


class ChangePasswordView(generics.UpdateAPIView):
    """Password change view class. Users must be authenticated"""
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.ChangePasswordSerializer

    def get_object(self):
        return User.objects.get(pk=self.request.user.id)


class LogoutView(APIView):
    """Disconnection View Class"""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        The user posts the token refresh.
        If it is valid, it is added to the blacklist.
        This token can no longer be used
        """
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response("Déconnecté")
        except Exception:
            raise ValidationError("Erreur de déconnexion")


class UsersListView(generics.ListAPIView):
    """
    View class of the list of users.
    The user must be identified
    """
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.UsersListSerializer
