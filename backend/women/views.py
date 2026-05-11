from django.shortcuts import render
from django.http import HttpResponse
from .models import TagPost, Women
from django.shortcuts import render, get_object_or_404
from .models import Women, Category
from .forms import AddPostForm
from django.shortcuts import redirect
import uuid
from .forms import UploadFileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

def handle_uploaded_file(f):
    name = f.name
    ext = ''

    if '.' in name:
        ext = name[name.rindex('.'):]
        name = name[:name.rindex('.')]

    suffix = str(uuid.uuid4())

    with open(f"uploads/{name}_{suffix}{ext}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@login_required
@permission_required('women.add_women', raise_exception=True)
def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)

        if form.is_valid():
            w = form.save(commit=False)
            w.author = request.user
            w.save()
            return redirect('home')

    else:
        form = AddPostForm()

    return render(request, 'women/addpage.html', {
        'title': 'Добавление статьи',
        'form': form
    })


menu = ["Главная", "Услуги", "Рассчитать стоимость"]

services_data = [
    {"id": 1, "title": "Химчистка ковров", "price": "от 1000 ₽"},
    {"id": 2, "title": "Химчистка мебели", "price": "от 1500 ₽"},
    {"id": 3, "title": "Стирка белья", "price": "от 400 ₽"},
]

from .models import Women

def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    return render(request, 'women/post.html', {
        'post': post
    })



def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)

    posts = Women.published.filter(cat_id=category.pk)

    data = {
        'title': f'Рубрика: {category.name}',
        'posts': posts,
        'cat_selected': category.pk,
    }

    return render(request, 'women/index.html', data)


def index(request):
    posts = Women.published.all()

    data = {
        'title': 'Главная страница',
        'menu': ["Главная", "Услуги", "Рассчитать", "О компании"],
        'posts': posts,   # ← ВАЖНО: тут БД
        'cat_selected': 0,
    }

    return render(request, 'women/index.html', data)




def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)

    posts = Women.published.filter(cat_id=category.pk)

    data = {
        'title': f'Рубрика: {category.name}',
        'posts': posts,
        'cat_selected': category.pk,
    }

    return render(request, 'women/index.html', data)




def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)

    posts = tag.tags.filter(is_published=True)  # ВАЖНО

    return render(request, 'women/index.html', {
        'posts': posts,
        'title': f'Тег: {tag.tag}',
        'cat_selected': None,
    })

def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)

    posts = tag.tags.filter(is_published=True)

    data = {
        'title': f'Тег: {tag.tag}',
        'posts': posts,
        'cat_selected': None,
    }

    return render(request, 'women/index.html', context=data)


from django.shortcuts import render, get_object_or_404

def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    return render(request, 'women/post.html', {
        'post': post,
        'title': post.title
    })

def account(request):
    return render(request, 'women/account.html', {
        'title': 'Личный кабинет'
    })

def services(request):
    return render(request, 'women/services.html', {
        'title': 'Услуги'
    })

def show_service(request, service_id):
    return HttpResponse(f"Услуга {service_id}")

@login_required
def about(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            handle_uploaded_file(form.cleaned_data['file'])

    else:
        form = UploadFileForm()

    return render(request, 'women/about.html', {
        'title': 'О сайте',
        'form': form
    })



cats_db = [
    {'id': 1, 'name': 'Уборка квартир'},
    {'id': 2, 'name': 'Химчистка'},
    {'id': 3, 'name': 'Генеральная уборка'},
]

def contacts(request):
    return render(request, 'women/contacts.html', {
        'title': 'Контакты'
    })