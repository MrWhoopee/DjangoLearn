from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.template.context_processors import request
from django.template.defaultfilters import slugify
from django.template.loader import render_to_string
from django.urls import reverse


# Create your views here.

menu = [{'title': "Про сторінку", 'url_name': 'about'},
        {'title': "Додати статтю", 'url_name': 'add_page'},
        {'title': "Фідбек", 'url_name': 'contact'},
        {'title': "Увійти", 'url_name': 'login'}
]

data_db = [
    {'id': 1, 'title': 'Анджеліна Джолі', 'content': '''<h1>Анджеліна Джолі</h1> (англ. Angelina Jolie [7], при народженні Войт (англ. Voight), раніше Джолі Пітт (англ. Jolie Pitt); нар. 4 червня 1975, Лос-Анджелес, Каліфорнія, США) — американська акторка кіно, телебачення та озвучування, кінорежисерка, сценаристка, продюсерка, фотомодель, посол доброї волі ООН.
    Лауреатка премії «Оскар», трьох премій «Золотий глобус» (перша акторка в історії, яка вигравала премію три роки поспіль) та двох «Премій Гільдії кіноакторів США».''', 'is_published': True},
    {'id': 2, 'title': 'Марго Роббі', 'content': 'Біографія Марго Роббі', 'is_published': False},
    {'id': 3, 'title': 'Джулія Робертс', 'content': 'Біографія Джулії Робертс', 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'Акторки'},
    {'id': 2, 'name': 'Співачки'},
    {'id': 3, 'name': 'Спортсменки'},
]

def index(request):

    data = {
        'title': 'Головна',
        'menu': menu,
        'posts': data_db,
        'cat_selected': 0,
    }
    return render(request,'women/index.html',context=data)


def about(request):
    return render(request,'women/about.html', {'title': 'Про сторінку','menu':menu})

def show_post(request,post_id):
    return HttpResponse(f"Show article id: {post_id}")


def addpage(request):
    return HttpResponse("Додати статтю")


def contact(request):
    return HttpResponse("Фідбек")


def login(request):
    return HttpResponse("Авторизація")

def show_category(request,cat_id):
    data = {
        'title': 'Відображення по рубрикам',
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=data)

def page_not_found(request,exception):
    return HttpResponseNotFound('<h1>Page not found(((</h1>')