from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse('Страница women')

def categories(request, catid):
    print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')

def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h2> Entered year is {year}</h2>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> pishov v sraku </h1>')