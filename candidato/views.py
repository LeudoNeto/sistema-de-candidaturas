from django.shortcuts import redirect, render
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth.decorators import login_required

from empresa.models import Vaga

# Create your views here.
@login_required(login_url="candidato login")
def index(request):
    user = request.user
    if str(user.groups.all()[0]) == 'empresas':
        context = {
            'empresa': True
        }
        return render(request, 'candidato_index.html', context)

    context = {
        'nome': user.first_name,
        'vagas_disponiveis': Vaga.objects.all()
    }
    return render(request, 'candidato_index.html', context)

def cadastro(request):
    if request.user.is_authenticated:
        return redirect('candidato index')
    if request.method == 'GET':
        return render(request, 'candidato_cadastro.html')
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username = email).first()

        if user:
            context = {
                'erro': True
            }
            return render(request, 'candidato_cadastro.html', context)

        user = User.objects.create_user(username = email, password = senha, first_name = nome)
        candidatos = Group.objects.get(name='candidatos')
        candidatos.user_set.add(user)
        django_login(request, user)
        context = {
            'cadastrado': True
        }
        return render(request, 'candidato_cadastro.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('candidato index')
    if request.method == 'GET':
        return render(request, 'candidato_login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(username = email, password = senha)

        if user:
            django_login(request, user)
            return redirect('candidato index')
        else:
            context = {
                'invalid': True
            }
            return render(request, 'candidato_login.html', context)