from django.shortcuts import render


def index(request):
    """Главная страница сервера"""
    return render(request, 'index.html')


def how_to_start(request):
    """Страница с инструкцией по подключению"""
    return render(request, 'how_to_start.html')


def states(request):
    """Страница с информацией о государствах"""
    countries = [
        {
            'id': 1,
            'name': 'Королевство Эрридия',
            'color': '#F0F0F0',  # Белый
            'slug': 'erridia'
        },
        {
            'id': 2,
            'name': 'Королевство Элора',
            'color': '#5DBCD2',  # Голубой
            'slug': 'elora'
        },
        {
            'id': 3,
            'name': 'Королевство Коловия',
            'color': '#2a2a2a',  # Чёрный
            'slug': 'koloviya'
        },
        {
            'id': 4,
            'name': 'Валкарионская Империя',
            'color': '#6B6B6B',  # Серый
            'slug': 'valkarion'
        },
        {
            'id': 5,
            'name': 'Альк Кадир',
            'color': '#D4AF37',  # Жёлтый
            'slug': 'alk-kadir'
        },
        {
            'id': 6,
            'name': 'Империя Великих Домов',
            'color': '#1E3A8A',  # Синий
            'slug': 'great-houses'
        },
        {
            'id': 7,
            'name': 'Королевство Алиола',
            'color': '#8B5CF6',  # Фиолетовый
            'slug': 'aliola'
        },
        {
            'id': 8,
            'name': 'Королевство Удов',
            'color': '#5EEAD4',  # Светло-бирюзовый
            'slug': 'udov'
        },
    ]
    return render(request, 'states.html', {'countries': countries})


from django.shortcuts import render
from django.http import Http404


def index(request):
    """Главная страница сервера"""
    return render(request, 'index.html')


def how_to_start(request):
    """Страница с инструкцией по подключению"""
    return render(request, 'how_to_start.html')


def states(request):
    """Страница с информацией о государствах"""
    countries = Country.objects.all().order_by('order', 'id')

    countries_list = [
        {
            'id': country.id,
            'name': country.name,
            'color': country.color,
            'slug': country.slug
        }
        for country in countries
    ]

    return render(request, 'states.html', {'countries': countries_list})


from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Country, Region  # Импортируем модели


def country_detail(request, slug):
    """Страница с информацией о конкретной стране"""

    # Получаем страну из базы данных
    country = get_object_or_404(Country, slug=slug)

    # Получаем все регионы этой страны
    regions = country.regions.all()

    # Получаем дополнительные данные из JSON поля
    extra_data = country.extra_data or {}

    # Преобразуем данные для шаблона
    country_data = {
        'name': country.name,
        'color': country.color,
        'flag': country.flag,
        'region_name': country.region_name,
        'general_info': {
            'politics': country.politics,
            'military': country.military,
            'language': extra_data.get('general_info', {}).get('language', ''),
            'religion': extra_data.get('general_info', {}).get('religion', ''),
            'income': country.income,
            'ruling_house': country.ruling_house,
            'current_ruler': country.current_ruler,
            'heir': country.heir,
            'fact': country.fact,
        },
        'regions': [
            {
                'name': region.name,
                'flag': region.flag,
                'description': region.description
            }
            for region in regions
        ],
    }

    # Добавляем религию (если есть)
    if 'religion' in extra_data:
        country_data['religion'] = extra_data['religion']

    # Добавляем язык (если есть)
    if 'language' in extra_data:
        country_data['language'] = extra_data['language']

    # Добавляем ярлства/тингства (если есть)
    if 'jarlstvos' in extra_data:
        country_data['jarlstvos'] = extra_data['jarlstvos']

    # Добавляем уезды (если есть)
    if 'uezds' in extra_data:
        country_data['uezds'] = extra_data['uezds']

    # Добавляем детали религии (для Валкариона)
    if 'religion_detail' in extra_data:
        country_data['religion_detail'] = extra_data['religion_detail']

    return render(request, 'country_detail.html', {
        'country': country_data,
        'slug': slug
    })

    # Временный редирект на главную страницу государств
    # Позже создадим отдельные шаблоны для каждой страны
    from django.http import HttpResponse
    return HttpResponse(f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{country_name} — GeoGamesMedieval</title>
            <style>
                body {{
                    background: #0a0a0f;
                    color: #f0f0f5;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    min-height: 100vh;
                    margin: 0;
                }}
                .container {{
                    text-align: center;
                    padding: 2rem;
                }}
                h1 {{
                    font-family: 'Cinzel', serif;
                    font-size: 2.5rem;
                    margin-bottom: 1rem;
                }}
                p {{
                    color: #b0b0c0;
                    font-size: 1.1rem;
                }}
                a {{
                    color: #d4af37;
                    text-decoration: none;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>{country_name}</h1>
                <p>Страница в разработке...</p>
                <p><a href="/states/">← Вернуться к государствам</a></p>
            </div>
        </body>
        </html>
    """)

def industrial(request):
    """Страница сервера GeoGames Industrial"""
    return render(request, 'industrial.html')

def rules(request):
    """Страница с правилами сервера"""
    return render(request, 'rules.html')

from .models import Alliance # Убедись, что импортировал Alliance

def alliances(request):
    alliances = Alliance.objects.all()
    return render(request, 'alliances.html', {'alliances': alliances})

def alliance_detail(request, slug):
    """Страница с информацией о конкретном союзе"""
    alliance = get_object_or_404(Alliance, slug=slug)
    return render(request, 'alliance_detail.html', {'alliance': alliance})