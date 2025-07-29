from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.template.context_processors import request
from django.template.loader import render_to_string
from django.urls import reverse


# Create your views here.

def index(request): # HttpRequest через цей клас буде доступна вся інформація про поточний запит
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)
    return render(request,'women/index.html')

def about(request):
    return render(request,'women/about.html')

def categories(request, cat_id):
    return HttpResponse(f'<h1>Categories</h1><p>id: {cat_id}</p>')


def categories_by_slug(request,cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Categories</h1><p>id(str): {cat_slug}</p>')

def archive(request, year):
    if int(year) > 2023:
        uri = reverse('cats', args=('music',))
        return redirect(uri) #301 messsage
    return HttpResponse(f'<h1>Archive by years</h1><p>{year}</p>')


def page_not_found(request,exception):
    return HttpResponseNotFound('<h1>Page not found(((</h1>')