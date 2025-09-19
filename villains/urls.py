from django.urls import path
from .views import lista_viloes , criar_viloes
from django.contrib import admin

urlpatterns = [
    path('lista/', lista_viloes, name='lista_viloes'),
    path('novo/', criar_viloes, name='criar_heroi'),
]



admin.site.site_header = "SuperBook Admin"
admin.site.site_title = "SuperBook Painel"
admin.site.index_title = "Bem-vindo ao SuperBook"