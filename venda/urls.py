from django.urls import path
from .views import listar

urlpatterns = [
    path('', listar, name='listar'),
]