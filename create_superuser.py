import os
import django

# 1. Сначала настраиваем Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GeoGamesMedieval.settings')
django.setup()

# 2. И только ПОСЛЕ этого импортируем User
from django.contrib.auth.models import User

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@geogames.ru',
        password='$RFV5tgb^YHN'
    )
    print("✅ Суперпользователь создан: admin / $RFV5tgb^YHN")
else:
    print("ℹ️ Пользователь уже существует.")
