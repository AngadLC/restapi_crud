from functools import partial
from django import views
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import students
# from restapi.crudapi.models import students
from .serializers import Studentserializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.
# @csrf_exempt
@method_decorator(csrf_exempt, name='dispatch')

class classbasedAPI(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        if id is not None:
            cru = students.objects.get(id=id)
            serializers = Studentserializers(cru)
            json_data = JSONRenderer().render(serializers.data)
            return HttpResponse(json_data,content_type='application/json')
        # if all have to be look
        stu = students.objects.all()
        serializers = Studentserializers(stu, many= True)
        # json_data = JSONRenderer().render(serializers.data)
        # return HttpResponse(json_data,content_type='application/json')
        data = serializers.data
        return JsonResponse(data, safe=False)

    # post method 
    def post(self, request, *args, **kwargs):
        json_data = request.body
        # print(json_data)
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        print(python_data)
        serializers = Studentserializers(data = python_data)
        if serializers.is_valid():
            serializers.save()
            res = {'mes':'data saved'}
            json_data= JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializers.errors)
        return HttpResponse(json_data, content_type= 'application/json')
    
    # update method
    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        cud = students.objects.get(id = id)
        serializers = Studentserializers(cud,data=python_data,partial= True)
        if serializers.is_valid():
            serializers.save()
            res = {'msg':'Data updated!'}
            return JsonResponse(res, safe=False)
        
    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        cud = students.objects.get(id = id)
        cud.delete()
        res = {'msg':'Data delete!'}
        return JsonResponse(res,safe=False)