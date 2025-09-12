from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import ClienteForm
import datetime


# Create your views here.
def horario_atual(request):
    horario_atual = datetime.datetime.now()
    return render(request, "lista_horario.html", {"horario_atual": horario_atual})


def exibir_template(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            print(request.POST)
            return HttpResponseRedirect("horario/")
    form = ClienteForm()
    return render(request, "form_template.html", {"form": form})
