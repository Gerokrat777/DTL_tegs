from django.shortcuts import render

# Create your views here.


def platform(request):
    return render(request, 'platform.html')


def games(request):
    page_name = "Игры"
    game_1 = "Atomic Heart"
    game_2 = "Cyberpunk"
    game_3 = "PayDay 2"
    buy = "Купить"
    context = {
        'Title': page_name,
        'game_1': game_1,
        'game_2': game_2,
        'game_3': game_3,
        'buy': buy,
    }
    return render(request, 'games.html', context)


def cart(request):
    page_name = "Корзина"
    img = "/static/Корзина.jpg"
    text_1 = "Здесь"
    text_2 = "ничего"
    text_3 = "НЕТ!"
    context = {
        'Title': page_name,
        'img': img,
        'text_1': text_1,
        'text_2': text_2,
        'text_3': text_3,
    }
    return render(request, 'cart.html', context)
