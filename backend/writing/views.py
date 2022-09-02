from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Writing
from .serializers import WritingSerializer

from rest_framework import permissions

class WritingAll(generics.ListCreateAPIView):
    queryset = Writing.objects.all()
    serializer_class = WritingSerializer

class WritingAIRPLANE(APIView):
    def get(self, request, format=None):
        queryset = Writing.objects.filter(board='airplane')
        serializer = WritingSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        request.data['board'] = 'airplane'
        serializer = WritingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WritingCAR(APIView):
    def get(self, request, format=None):
        queryset = Writing.objects.filter(board='car')
        serializer = WritingSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        request.data['board'] = 'car'
        serializer = WritingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WritingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Writing.objects.all()
    serializer_class = WritingSerializer