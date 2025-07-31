from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render, get_object_or_404
from women.models import Women, Category

# Create your views here.

menu = [{'title': "Про сторінку", 'url_name': 'about'},
        {'title': "Додати статтю", 'url_name': 'add_page'},
        {'title': "Фідбек", 'url_name': 'contact'},
        {'title': "Увійти", 'url_name': 'login'}
]


def index(request):
    posts = Women.published.all()
    data = {
        'title': 'Головна',
        'menu': menu,
        'posts': posts,
        'cat_selected': 0,
    }
    return render(request,'women/index.html',context=data)


def about(request):
    return render(request,'women/about.html', {'title': 'Про сторінку','menu':menu})

def show_post(request,post_slug):
    post = get_object_or_404(Women,slug=post_slug)
    data = {'title': post.title,
            'menu': menu,
            'post': post,
            'cat_selected': 1}

    return render(request,'women/post.html',data)


def addpage(request):
    return HttpResponse("Додати статтю")


def contact(request):
    return HttpResponse("Фідбек")


def login(request):
    return HttpResponse("Авторизація")

def show_category(request,cat_slug):
    category = get_object_or_404(Category,slug=cat_slug)
    posts = Women.published.filter(cat_id=category.pk)

    data = {
        'title': f'Рубрика: {category.name}',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, 'women/index.html', context=data)

def page_not_found(request,exception):
    return HttpResponseNotFound('<h1>Page not found(((</h1>')