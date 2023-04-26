from django.urls import path
from . import views

urlpatterns = [
    #urls de doação
    path('doacao/solicitar/', views.solicitar_doacao, name='solicitar_doacao'),
    path('doacao/cancelar/<int:id>/', views.cancelar_solicitacao, name='cancelar_solicitacao'),
    path('doacao/analisar/<int:id>/', views.analisar_solicitacao, name='analisar_solicitacao'),
    path('doacao/listar/', views.listar_doacao, name='listar_doacao'),
    #urls de peruca
    path('criar_peruca/', views.criar_peruca, name='criar_peruca'),
    path('editar_peruca/<int:id>/', views.editar_peruca, name='editar_peruca'),
    path('excluir_peruca/<int:id>/', views.excluir_peruca, name='excluir_peruca'),
    path('listar_perucas/', views.listar_perucas, name='listar_perucas'),
]
