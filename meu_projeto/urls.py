from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('admin/', admin.site.urls),
    path('candidato/', include('candidato.urls')),
    path('empresa/', include('empresa.urls')),
    path('logout', views.logout, name = 'logout'),
    path('mudar_grupo', views.mudar_grupo, name = 'mudar grupo')
]
