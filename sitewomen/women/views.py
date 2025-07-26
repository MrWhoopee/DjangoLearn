from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request): # HttpRequest через цей клас буде доступна вся інформація про поточний запит
    return HttpResponse('Page Women App')

def categories(request):
    return HttpResponse('<h1>Categories</h1>')
