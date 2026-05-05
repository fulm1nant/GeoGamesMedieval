import os
import django

# 1. Сначала настраиваем Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GeoGamesMedieval.settings')
django.setup()

# 2. Только ПОСЛЕ этого импортируем модели
from django.contrib.auth.models import User

# 3. Логика создания
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='',
        password='$RFV5tgb^YHN'
    )
    print("✅ Суперпользователь создан!")
    print("   Логин: admin")
    print("   Пароль: $RFV5tgb^YHN")
else:
    print("ℹ️ Суперпользователь уже существует.")
