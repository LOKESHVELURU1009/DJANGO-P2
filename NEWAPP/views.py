from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def loki(request):
    return HttpResponse('loki is best coder')