from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar_aposta/', views.cadastrar_aposta, name='cadastrar_aposta'),
    path('trata_aposta/', views.trata_aposta, name='trata_aposta'),
    path('ver_apostas/', views.ver_apostas, name='ver_apostas'),
    path('excluir_apostas/<int:id>', views.excluir_apostas, name='excluir_apostas'),
    path('edita_apostas/<int:id>', views.edita_apostas, name='edita_apostas'),
    path('salva_apostas/<int:id>', views.salva_apostas, name='salva_apostas'),
    path('sync/', views.sync, name='sync'),
    path('estrategias/', views.estrategias, name='estrategias')
]
