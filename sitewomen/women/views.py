from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.template.context_processors import request
from django.template.defaultfilters import slugify
from django.template.loader import render_to_string
from django.urls import reverse


# Create your views here.

menu = ['Site About','Add article','Feedback','Sing up']

class MyClass:
    def __init__(self,a,b):
        self.a = a
        self.b = b


def index(request): # HttpRequest через цей клас буде доступна вся інформація про поточний запит
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)
    data = {
        'title': 'main Page',
        'menu': menu,
        'float': 28.56,
        'lst': [1,2,'abc',True],
        'set': (1,2,3,4),
        'dict': {'key1': 1, 'key2': 2},
        'obj': MyClass(10,20),
        'url': slugify('The main Page'),

    }
    return render(request,'women/index.html',context=data)

def about(request):
    return render(request,'women/about.html', {'title': 'About Page'})

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