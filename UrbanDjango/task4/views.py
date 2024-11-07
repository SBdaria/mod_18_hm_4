from django.shortcuts import render

def homepage(request):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'fourth_task/homepage.html', context)

def clothespage(request):
    context = {
        'title': 'Одежда',
        'clothes': [
            'Верхняя одежда',
            'Платья',
            'Рубашки и блузки',
            'Футболки и топы',
            'Брюки и шорты',
            'Юбки',
            'Сумки и аксессуары'
        ]
    }
    return render(request, 'fourth_task/clothes.html', context)

def shoespage(request):
    context = {
        'title': 'Обувь',
        'shoes': [
            'Зимняя обувь',
            'Летняя обувь',
            'Кроссовки'
        ]
    }
    return render(request, 'fourth_task/shoes.html', context)
