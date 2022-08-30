from django.shortcuts import render
from rest_framework import generics

from .models import Writing
from .serializers import WritingSerializer

from rest_framework import permissions

class WritingAll(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Writing.objects.all()
    serializer_class = WritingSerializer

class WritingAIRPLANE(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Writing.objects.filter(board='airplane')
    serializer_class = WritingSerializer

class WritingCAR(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Writing.objects.filter(board='car')
    serializer_class = WritingSerializer

class WritingDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Writing.objects.all()
    serializer_class = WritingSerializer


