from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('how-to-start/', views.how_to_start, name='how_to_start'),
    path('states/', views.states, name='states'),
    path('states/<slug:slug>/', views.country_detail, name='country_detail'),
    path('alliances/', views.alliances, name='alliances'),
    path('industrial/', views.industrial, name='industrial'),
    path('rules/', views.rules, name='rules'),
    path('alliances/', views.alliances, name='alliances'),
    path('alliances/<slug:slug>/', views.alliance_detail, name='alliance_detail'),
]
