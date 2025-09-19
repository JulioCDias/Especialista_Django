from django.urls import path, include

from .views import (
    ClienteCreateView,
    ClienteListView,
    ClienteUpdateView,
    ClienteDetailView,
    ClienteDeleteView,
)

app_name = "app"

urlpatterns = [
    path("form_cliente", ClienteCreateView.as_view(), name="form_cliente"),
    path("lista_clientes", ClienteListView.as_view(), name="lista_clientes"),
    path("form_cliente/<int:pk>", ClienteUpdateView.as_view(), name="update_cliente"),
    path("detail_cliente/<int:pk>", ClienteDetailView.as_view(), name="detail_cliente"),
    path("delete_cliente/<int:pk>", ClienteDeleteView.as_view(), name="delete_cliente"),
]
