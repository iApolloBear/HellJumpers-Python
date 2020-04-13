from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from .serializers import UserSerializer, UserWalletSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class UserCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRegistration(APIView):
    def post(self, request, format=None):
        wallet = UserWalletSerializer(data=request.data)

        if wallet.is_valid(raise_exception=ValueError):
            wallet.create(validated_data=request.data)
            return Response(wallet.data, status=status.HTTP_201_CREATED)
        else:
            return Response(wallet.error_messages, status=status.HTTP_400_BAD_REQUEST)
