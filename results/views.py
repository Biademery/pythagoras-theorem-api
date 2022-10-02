from django.shortcuts import render
from rest_framework import viewsets
from .models import Result
from .serializers import ResultSerializers

class ResultView(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializers