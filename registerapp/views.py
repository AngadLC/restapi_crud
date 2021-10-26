from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import registerSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def register_create(request):
    if request.method == "POST":
        json_data = request.body
        # print(json_data)
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        print(python_data)
        serializers = registerSerializer(data = python_data)
        if serializers.is_valid():
            serializers.save()
            res = {'mes':'data saved'}
            json_data= JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer.render(serializers.errors)
        return HttpResponse(json_data, content_type= 'application/json')
    return HttpResponse("hi")