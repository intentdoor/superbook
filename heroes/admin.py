
from django.contrib import admin
from .models import Hero

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ['codinome', 'nome_real', 'poder_principal', 'cidade', 'criado_em' , 'email_contato']
    list_filter = ['cidade']
    search_fields = ['codinome', 'nome_real', 'cidade']

    fieldsets = (
        ('Identidade Secreta', {
            'fields': ('codinome', 'nome_real')
        }),
        ('Informações Gerais', {
            'fields': ('poder_principal', 'cidade', 'historia' , 'email_contato' , 'imagem')
        }),
        ('Dados de Registro', {
            'fields': ('criado_em',)
        }),
    )
    readonly_fields = ['criado_em']

