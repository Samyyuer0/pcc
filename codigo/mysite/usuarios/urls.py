from django.urls import path
from . import views

urlpatterns = [
    #urls de pessoa
    path('cadastrar_pessoa/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
    path('editar_pessoa/<int:id>/', views.editar_pessoa, name='editar_pessoa'),
    path('excluir_pessoa/<int:id>/', views.excluir_pessoa, name='excluir_pessoa'),
    path('criar_depoimento/', views.criar_depoimento, name='criar_depoimento'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    #urls de depoimento
    path('editar_depoimento/<int:pk>/', views.editar_depoimento, name='editar_depoimento'),
    path('excluir_depoimento/<int:pk>/', views.excluir_depoimento, name='excluir_depoimento'),
    path('listar_depoimentos/', views.listar_depoimentos, name='listar_depoimentos'),
    #urls de endeço
    path('criar_endereco/', views.criar_endereco, name='criar_endereco'),
    path('editar_endereco/<int:id>/', views.editar_endereco, name='editar_endereco'),
    path('excluir_endereco/<int:id>/', views.excluir_endereco, name='excluir_endereco'),
    path('listar_enderecos/', views.listar_enderecos, name='listar_enderecos'),
]
