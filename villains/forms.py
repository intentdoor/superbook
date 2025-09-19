from django import forms
from .models import Villain

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100, required=True, label="Seu nome")
    email = forms.EmailField(required=True, label="E-mail")
    mensagem = forms.CharField(widget=forms.Textarea, required=True)


class VillainForm(forms.ModelForm):
    class Meta:
        model = Villain
        fields = ['codinome', 'nome_real', 'poder_principal', 'cidade', 'historia' , 'email_contato']