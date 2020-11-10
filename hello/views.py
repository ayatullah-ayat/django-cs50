from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('Hello world')

def brian(request):
    return HttpResponse('Hello brian')

def mallan(request):
    return HttpResponse('Hello Mallan')

def greet(request, name):
    return HttpResponse(f"Hello {name}")