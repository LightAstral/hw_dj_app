from django.shortcuts import render


# Create your views here.


def home(request):
    context = {
        'page_title': 'Главная',
        'content': 'Это страница Главная о автомобилях.'
    }
    return render(request, 'cars_app/home.html', context)


def toyota(request):
    context = {
        'page_title': 'Тойота',
        'content': 'Это страница о Тойоте.'
    }
    return render(request, 'cars_app/toyota.html', context)


def honda(request):
    context = {
        'page_title': 'Хонда',
        'content': 'Это страница о Хонде.'
    }
    return render(request, 'cars_app/honda.html', context)


def renault(request):
    context = {
        'page_title': 'Рено',
        'content': 'Это страница о Рено.'
    }
    return render(request, 'cars_app/renault.html', context)
