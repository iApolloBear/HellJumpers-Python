from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from .serializers import UserSerializer, UserWalletSerializer, PromocionSerializer, ConcursoSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Concurso, Promocion, Client
from pyexcel_xls import get_data as xls_get
from pyexcel_xlsx import get_data as xlsx_get
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.


class UserRegistration(APIView):
    def post(self, request, format=None):
        wallet = UserWalletSerializer(data=request.data)

        if wallet.is_valid(raise_exception=ValueError):
            wallet.create(validated_data=request.data)
            return Response(wallet.data, status=status.HTTP_201_CREATED)
        else:
            return Response(wallet.error_messages, status=status.HTTP_400_BAD_REQUEST)


class PromocioListCreateView(ListCreateAPIView):
    queryset = Promocion.objects.all()
    serializer_class = PromocionSerializer


class ConcursoListCreateView(ListCreateAPIView):
    queryset = Concurso.objects.all()
    serializer_class = ConcursoSerializer()


class ExcelParser(APIView):
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
