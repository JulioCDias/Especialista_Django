from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)
from .models import Cliente
# Create your views here.


class ClienteCreateView(CreateView):
    model = Cliente
    fields = "__all__"
    template_name = "form_template.html"
    success_url = "lista_clientes"


class ClienteListView(ListView):
    model = Cliente
    template_name = "lista_templates.html"
    context_object_name = "clientes"


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "detail_cliente.html"
    context_object_name = "cliente"


class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = "__all__"
    template_name = "form_template.html"
    success_url = reverse_lazy("app:lista_clientes")
