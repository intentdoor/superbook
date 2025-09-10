from django.db import models

# Arthur Américo

class Villain(models.Model):
    codinome = models.CharField(max_length=50, unique=True)
    nome_real = models.CharField(max_length=100, blank=True, null=True)
    poder_principal = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    historia = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    email_contato = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.codinome