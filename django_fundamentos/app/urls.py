from django.urls import path
from . import views

urlpatterns = [
    path("horario/", views.horario_atual),
    path("form/", views.exibir_template),
]
