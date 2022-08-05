from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'empresa index'),
    path('cadastro', views.cadastro, name = 'empresa cadastro'),
    path('login', views.login, name = 'empresa login'),
    path('criar_vaga', views.criar_vaga, name = 'empresa criar vaga'),
    path('deletar_vaga', views.deletar_vaga, name = 'deletar vaga'),
    path('editar_vaga', views.editar_vaga, name = 'editar vaga'),
    path('editar_vaga2', views.editar_vaga2, name = 'editar vaga2'),
    path('detalhes_vaga', views.detalhes_vaga, name = 'detalhes vaga'),
]