from django.http import HttpResponse
from django.shortcuts import render
import json
import os
from pathlib import Path
from ematiq import settings
# Create your views here.

def main(request):
    return render(request, 'main.html')

# def get_file(request):
#     directory= 'static/File.json'
#     f=open(directory)
#     return HttpResponse(f.read(),mimetype='text/plain')

def get_file(request):

    #json_data = open('/static/File.json')  
    json_data_dir = os.path.join(settings.BASE_DIR, 'static', "File.json")
    json_data = open(json_data_dir) 
    data1 = json.load(json_data) # deserialises it
    data2 = json.dumps(data1) # json formatted string

    json_data.close()
    return HttpResponse(data2)

def refresh(request):
    return render(request, 'refresh.php')