from django.shortcuts import render
from rest_framework import generics
from .models import BoardingHouse
from .serializers import BoardingHouseSerializer

class BoardingHouseListCreate(generics.ListCreateAPIView):
    queryset = BoardingHouse.objects.all()
    serializer_class = BoardingHouseSerializer

class BoardingHouseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoardingHouse.objects.all()
    serializer_class = BoardingHouseSerializer
