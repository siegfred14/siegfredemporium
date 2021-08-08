from django.shortcuts import render
from rest_framework import GenericAPIView, serializers
from .serializers import UserSerializer

# Create your views here.


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
