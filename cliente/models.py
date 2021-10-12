from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django import forms

class Cliente(models.Model):
    id_cli = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=12)
    telefone = models.CharField(max_length=16)
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)

class form_cliente(forms.ModelForm):
    class Meta:
        model = Cliente
        exclude = ('',)