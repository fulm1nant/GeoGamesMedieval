from django.contrib.auth.models import User
from django.db import models


class Country(models.Model):
    name = models.CharField('Название', max_length=100)
    slug = models.SlugField('URL-адрес', unique=True)
    color = models.CharField('Цвет темы', max_length=50, default='#333333')
    flag = models.CharField('Путь к флагу', max_length=200, blank=True)
    region_name = models.CharField('Название регионов', max_length=50, default='Регионы')
    order = models.PositiveIntegerField('Порядок отображения', default=0)

    # Основная информация
    politics = models.TextField('Политика', blank=True)
    military = models.TextField('Военная политика', blank=True)
    income = models.TextField('Доход', blank=True)
    ruling_house = models.CharField('Правящий род', max_length=100, blank=True)
    current_ruler = models.CharField('Текущий правитель', max_length=100, blank=True)
    heir = models.CharField('Наследник', max_length=100, blank=True)
    fact = models.TextField('Интересный факт', blank=True)

    # ✨ НОВОЕ ПОЛЕ: Хранит язык, религию, тингства, уезды и всё остальное
    extra_data = models.JSONField('Дополнительные данные (язык, религия, тингства, уезды)', blank=True, null=True)

    def __str__(self):
        return self.name


class Region(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Страна', related_name='regions')
    name = models.CharField('Название', max_length=100)
    flag = models.CharField('Путь к флагу', max_length=200, blank=True)
    description = models.TextField('Описание', blank=True)

# 🆕 НОВАЯ МОДЕЛЬ: Привязка пользователя к стране
class CountryAccess(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='country_access')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Страна')

    def __str__(self):
            return f"{self.user.username} → {self.country.name}"

    class Meta:
            verbose_name = 'Доступ к стране'
            verbose_name_plural = 'Доступы к странам'


class Alliance(models.Model):
    name = models.CharField('Название', max_length=200)
    slug = models.SlugField('Адрес страницы', unique=True)
    flag = models.CharField('Ссылка на флаг', max_length=200)
    goal = models.TextField('Цель')
    alliance_type = models.CharField('Тип', max_length=100)
    # Участники (связь со странами)
    members = models.ManyToManyField(Country, verbose_name='Участники', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Союз'
        verbose_name_plural = 'Союзы'