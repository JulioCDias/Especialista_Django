from django import forms


class ClienteForm(forms.Form):
    nome = forms.CharField(label="Nome do Cliente", max_length=100)
    idade = forms.IntegerField(label="Idade do Cliente")
    email = forms.EmailField(label="Email do Cliente", max_length=150)
    data_nascimento = forms.DateField(label="Data de Nascimento do Cliente")
    is_ativo = forms.BooleanField(label="Cliente Ativo")
