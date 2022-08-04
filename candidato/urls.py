from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'candidato index'),
    path('cadastro', views.cadastro, name = 'candidato cadastro'),
    path('login', views.login, name = 'candidato login'),
]