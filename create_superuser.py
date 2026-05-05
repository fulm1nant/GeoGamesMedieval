import os
import django
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GeoGamesMedieval.settings')
django.setup()

# Создаём суперпользователя
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@geogames.ru',  # можешь поменять на свой
        password='admin123'          # пароль (поменяй потом в админке!)
    )
    print("✅ Суперпользователь создан!")
    print("   Логин: admin")
    print("   Пароль: admin123")
else:
    print("ℹ️ Суперпользователь уже существует.")
