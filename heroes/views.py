from django.shortcuts import render
from .models import Hero
from django.views.generic import ListView


def lista_herois(request):
    herois = Hero.objects.all()  # busca todos os heróis do banco
    return render(request, "heroes/lista_herois.html", {"herois": herois})

class HeroListView(ListView):
    model = Hero
    template_name = "heroes/lista_herois.html"
    context_object_name = "herois"