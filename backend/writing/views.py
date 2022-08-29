from django.shortcuts import render
from rest_framework import generics

from .models import Writing
from .serializers import WritingSerializer

class WritingAll(generics.ListCreateAPIView):
    queryset = Writing.objects.all()
    serializer_class = WritingSerializer

class WritingAIRPLANE(generics.ListCreateAPIView):
    queryset = Writing.objects.filter(board='airplane')
    serializer_class = WritingSerializer

class WritingCAR(generics.ListCreateAPIView):
    queryset = Writing.objects.filter(board='car')
    serializer_class = WritingSerializer

class WritingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Writing.objects.all()
    serializer_class = WritingSerializer


