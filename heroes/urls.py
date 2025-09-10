
from django.urls import path
from .views import HeroListView , lista_herois , contato_view , criar_heroi
from django.contrib import admin

urlpatterns = [
    path('lista/', lista_herois, name='lista_herois'),
    path('cbv-lista/', HeroListView.as_view(), name='cbv_lista_herois'),
    path('contato/', contato_view, name='contato'),
    path('novo/', criar_heroi, name='criar_heroi'),
]


admin.site.site_header = "SuperBook Admin"
admin.site.site_title = "SuperBook Painel"
admin.site.index_title = "Bem-vindo ao SuperBook"


