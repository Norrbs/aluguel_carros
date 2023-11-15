from django.urls import path
from .views import ListarTemplateView, DetalharTemplateView, AdicionarTemplateView, AtualizarTemplateView, DeletarTemplateView

urlpatterns = [
    path('', ListarTemplateView.as_view(), name='listar'),
    path('<int:pk>', DetalharTemplateView.as_view(), name='detalhar'),
    path('adicionar/', AdicionarTemplateView.as_view(), name='adicionar'),
    path('atualizar/<int:pk>', AtualizarTemplateView.as_view(), name='atualizar'),
    path('deletar/<int:pk>', DeletarTemplateView.as_view(), name='deletar')
]