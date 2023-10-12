from django.urls import path
from .views import listar, detalhar, adicionar, atualizar, deletar

urlpatterns = [
    path('', listar, name='listar'),
    path('<int:id>', detalhar, name='detalhar'),
    path('adicionar/', adicionar, name='adicionar'),
    path('atualizar/<int:id>', atualizar, name='atualizar'),
    path('deletar/<int:id>', deletar, name='deletar')
]