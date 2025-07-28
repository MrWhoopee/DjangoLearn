from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request): # HttpRequest через цей клас буде доступна вся інформація про поточний запит
    return HttpResponse('Page Women App')

def categories(request, cat_id):
    return HttpResponse(f'<h1>Categories</h1><p>id: {cat_id}</p>')


def categories_by_slug(request,cat_slug):
    return HttpResponse(f'<h1>Categories</h1><p>id: {cat_slug}</p>')

def archive(request,year):
    return HttpResponse(f'<h1>Archive by years</h1><p>{year}</p>')