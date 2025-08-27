
from django.urls import path
from .views import HeroListView , lista_herois

urlpatterns = [
    path('lista/', lista_herois, name='lista_herois'),
    path('cbv-lista/', HeroListView.as_view(), name='cbv_lista_herois'),
]