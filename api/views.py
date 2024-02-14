from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.shortcuts import render

from base.models import StockData
from .serializer import StockDataSerializer

# Create your views here.

class CheckHealth(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        return Response({ "message": "api is working" })

class StockDataView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, symbol):
        try:
            results = StockData.objects.filter(symbol=symbol).values()
            serializer = StockDataSerializer(results, many=True)
            print(serializer.data)
            return Response(serializer.data)
        except Exception as err:
            print(err)
            return Response({ "error": "Could not fetch data" })