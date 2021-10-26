from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from .models import students
from .serializers import Studentserializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
class classbasedAPI(APIView):
    def get(self, request,pk = None, format = None):
        id = pk
        if id is not None:
            cru = students.objects.get(id=id)
            serializers = Studentserializers(cru)
            return Response(serializers.data, status=status.HTTP_200_OK)
        # if all have to be look
        stu = students.objects.all()
        serializers = Studentserializers(stu, many= True)
        return Response(serializers.data)
    # post method 
    def post(self, request, format= None):
        serializers = Studentserializers(data = request.data)
        if serializers.is_valid():
            serializers.save()
            res = {'mes':'data saved'}
            return Response(res, status= status.HTTP_201_CREATED)
    # update method
    def put(self, request, pk = None, format = None ):
        id = pk
        cud = students.objects.get(id = id)
        serializers = Studentserializers(cud,data=request.data)
        if serializers.is_valid():
            serializers.save()
            res = {'msg':'Data updated!'}
            return Response(res)
        return Response(serializers.errors,status= status.HTTP_400_BAD_REQUEST)
    def patch(self, request, pk = None, fromat = None):
        id = pk 
        cud = students.objects.get(id = id)
        serializers = Studentserializers(cud,data=request.data, partial = True)
        if serializers.is_valid():
            serializers.save()
            res = {'msg':'Data updated!'}
            return Response(res)
        return Response(serializers.errors,status= status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk = None, format = None):
        id = pk
        cud = students.objects.get(id = id)
        cud.delete()
        res = {'msg':'Data delete!'}
        return Response(res, status = status.HTTP_200_OK)