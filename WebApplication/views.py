from json import dumps
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def get_json(request):
    print("11111111111")
    resp = "i"
    return HttpResponse(dumps(resp),content_type='application/json')