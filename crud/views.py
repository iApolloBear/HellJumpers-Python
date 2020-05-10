from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from .serializers import UserSerializer, UserWalletSerializer, PromocionSerializer, ConcursoSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Concurso, Promocion, Client, UserWallet
from pyexcel_xls import get_data as xls_get
from pyexcel_xlsx import get_data as xlsx_get
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class Hello(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = UserWallet.objects.get(pk=request.user.pk)
        serializer = UserWalletSerializer(user)
        return Response(serializer.data)


class UserList(ListCreateAPIView):
    queryset = UserWallet.objects.all()
    serializer_class = UserWalletSerializer


class UserRegistration(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        wallet = UserWalletSerializer(data=request.data)

        if wallet.is_valid(raise_exception=ValueError):
            wallet.create(validated_data=request.data)
            return Response(wallet.data, status=status.HTTP_201_CREATED)
        else:
            return Response(wallet.error_messages, status=status.HTTP_400_BAD_REQUEST)


class PromocioListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Promocion.objects.all()
    serializer_class = PromocionSerializer

    def list(self, request):
        queryset = Promocion.objects.filter(promo_wallet=request.user.id)
        serializer = PromocionSerializer(queryset, many=True)
        return Response(serializer.data)


class ConcursoListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Concurso.objects.all()
    serializer_class = ConcursoSerializer

    def list(self, request):
        queryset = Concurso.objects.filter(contest_wallet=request.user.id)
        serializer = ConcursoSerializer(queryset, many=True)
        return Response(serializer.data)


class ExcelParser(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        try:
            excel_file = request.FILES['excel_file']
            if str(excel_file).split('.')[-1] == "xls":
                data = xls_get(excel_file, column_limit=5)
            elif str(excel_file).split('.')[-1] == "xlsx":
                data = xlsx_get(excel_file, column_limit=5)
            else:
                return HttpResponse("Invalid File")

            details = data["Detalle"]
            if len(details) > 1:
                for detail in details:
                    if len(detail) > 0 and detail[0] != "Sucursal":
                        Client.objects.create(
                            sucursal=detail[0], cartera=detail[1], clientes=detail[2], fecha_alta=detail[3], saldo=detail[4])
            return HttpResponse("Data Readed")

        except MultiValueDictKeyError:
            return HttpResponse("Invalid File")
