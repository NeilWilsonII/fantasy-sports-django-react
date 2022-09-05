from django.shortcuts import render
from .models import EPLPlayer
from .serializers import EPLSerializer
from rest_framework import generics
# Create your views here.
class ListPlayers(generics.ListAPIView):
    queryset = EPLPlayer.objects.all()
    serializer_class = EPLSerializer