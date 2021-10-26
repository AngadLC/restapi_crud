from django.shortcuts import render
from django.shortcuts import render
# from rest_framework.serializers import Serializer
from .models import students
from .serializers import Studentserializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET','POST','PUT','DELETE'])
# Create your views here.
def crud(request, pk = None):
    if request.method == "POST":
        serializers = Studentserializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':"Data created"})
        return Response(serializers.errors)
    if request.method == 'GET':
        # print(request.data)
        # using browsers
        # id = pk
        # third party application
        id = request.data.get('id')
        if id is not None:
            cru = students.objects.get(id=id)
            serializers = Studentserializers(cru)
            return Response(serializers.data) 
        # if all have to be look
        stu = students.objects.all()
        serializers = Studentserializers(stu, many= True)
        return Response(serializers.data)
    if request.method == 'PUT':
        id = request.data.get('id')
        stu = students.objects.get(pk = id)
        serializers = Studentserializers(stu, data=request.data, partial = True)
        if serializers.is_valid():
            serializers.save()
            return Response({'Msg':"Updated sucessful"})
        return Response(serializers.errors)
    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = students.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'deleted'})