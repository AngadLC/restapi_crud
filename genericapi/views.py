from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from .models import students
from .serializers import Studentserializers
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework import serializers, status
from django.contrib.auth.models import User
# Create your views here.
class classbasedAPI(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = Studentserializers
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = Studentserializers(queryset, many=True)
        return Response(serializer.data)
