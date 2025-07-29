from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.template.context_processors import request
from django.template.defaultfilters import slugify
from django.template.loader import render_to_string
from django.urls import reverse


# Create your views here.

menu = [{'title': "About site page", 'url_name': 'about'},
        {'title': "Add post", 'url_name': 'add_page'},
        {'title': "Feedback", 'url_name': 'contact'},
        {'title': "Login", 'url_name': 'login'}
]

data_db = [
    {'id': 1, 'title': 'Анджеліна Джолі', 'content': 'Біографія Анджеліни Джолі', 'is_published': True},
    {'id': 2, 'title': 'Марго Роббі', 'content': 'Біографія Марго Роббі', 'is_published': False},
    {'id': 3, 'title': 'Джулія Робертс', 'content': 'Біографія Джулії Робертс', 'is_published': True},
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

def show_post(request,post_id):
    return HttpResponse(f"Show article id: {post_id}")


def addpage(request):
    return HttpResponse("Adding page")


def contact(request):
    return HttpResponse("Feedback")


def login(request):
    return HttpResponse("Authorisation")

def page_not_found(request,exception):
    return HttpResponseNotFound('<h1>Page not found(((</h1>')