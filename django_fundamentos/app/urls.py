from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path("horario/", views.horario_atual, name="horario"),
    path("form/", views.exibir_template, name="form"),
]
