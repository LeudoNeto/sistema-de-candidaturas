from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'candidato index'),
    path('cadastro', views.cadastro, name = 'candidato cadastro'),
    path('login', views.login, name = 'candidato login'),
    path('inscricao', views.inscricao, name = 'candidato inscricao'),
    path('realizar_inscricao', views.realizar_inscricao, name = 'candidato realizar inscricao'),
    path('cancelar_inscricao', views.cancelar_inscricao, name = 'candidato cancelar inscricao'),
]