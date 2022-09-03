from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *

menu = ['О сайте', 'Добавить статью', 'Обратная свзяь', 'Войти']
def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'title': 'Главная страница', 'menu': menu, 'posts': posts})

def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте', 'menu': menu})

def categories(request, catid):
    print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')

def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h2> Entered year is {year}</h2>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> pishov v sraku </h1>')