from django import template
from women.models import *
from django.http import Http404

register = template.Library()

@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if filter is None:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)

@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if sort is None:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {'cats': cats, 'cat_selected': cat_selected}

@register.inclusion_tag('women/sidebar_left.html')
def show_sidebar(cat_selected=0):
    return {'cat_selected': cat_selected}

@register.inclusion_tag('women/main_menu.html')
def show_main_menu():
    menu = [
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
    ]
    return {'menu': menu}

@register.inclusion_tag('women/posts.html')
def show_posts(cat_slug=0):
    if cat_slug == 0:
        posts = Women.objects.all()
    else:
        cat_id = Category.objects.get(slug=cat_slug)
        posts = Women.objects.filter(cat_id=cat_id)
    if len(posts) == 0:
        raise Http404()

    return {'posts': posts}