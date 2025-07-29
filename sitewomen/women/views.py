from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.template.context_processors import request
from django.template.defaultfilters import slugify
from django.template.loader import render_to_string
from django.urls import reverse


# Create your views here.

menu = ['Site About','Add article','Feedback','Sing up']

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулии Робертс', 'is_published': True},
]

def index(request):

    data = {
        'title': 'Main Page',
        'menu': menu,
        'posts': data_db,

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