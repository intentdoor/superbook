from django.shortcuts import render , redirect
from .models import Villain
from django.views.generic import ListView
from .forms import VillainForm 

def lista_viloes(request):
    viloes = Villain.objects.all() 
    return render(request, "villains/lista_viloes.html", {"viloes": viloes})

class VillainsListView(ListView):
    model = Villain
    template_name = "villains/lista_viloes.html"
    context_object_name = "viloes"


def criar_viloes(request):
    if request.method == "POST":
        form = VillainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_viloes')
    else:
        form = VillainForm()

    return render(request, "villains/form_viloes.html", {"form": form})