from django.shortcuts import redirect, render
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth.decorators import login_required

from empresa.models import Vaga

# Create your views here.
@login_required(login_url="empresa login")
def index(request):
    user = request.user

    if str(user.groups.all()[0]) == 'candidatos':
        context = {
            'candidato': True
        }
        return render(request, 'empresa_index.html', context)
        
    vagas = Vaga.objects.filter(email_da_empresa = user.username)
    context = {
        'nome': user.first_name,
        'vagas': vagas,
        'num_de_candidatos': len(vagas)
    }
    return render(request, 'empresa_index.html', context)

def cadastro(request):
    if request.user.is_authenticated:
        return redirect('empresa index')
    if request.method == 'GET':
        return render(request, 'empresa_cadastro.html')
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username = email).first()

        if user:
            context = {
                'erro': True
            }
            return render(request, 'empresa_cadastro.html', context)

        user = User.objects.create_user(username = email, password = senha, first_name = nome)
        empresas = Group.objects.get(name='empresas')
        empresas.user_set.add(user)
        django_login(request, user)
        context = {
            'cadastrado': True
        }
        return render(request, 'empresa_cadastro.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('empresa index')
    if request.method == 'GET':
        return render(request, 'empresa_login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(username = email, password = senha)

        if user:
            django_login(request, user)
            return redirect('empresa index')
        else:
            context = {
                'invalid': True
            }
            return render(request, 'empresa_login.html', context)

@login_required(login_url="empresa login")
def criar_vaga(request):
    if request.method == "GET":
        return render(request, 'empresa_vaga.html')
    else:
        vaga = Vaga(
            nome = request.POST.get('nome'),
            faixa_salarial = request.POST.get('faixa_salarial'),
            escolaridade = request.POST.get('escolaridade'),
            nome_da_empresa = request.user.first_name,
            email_da_empresa = request.user.username
        )

        vaga.save()
        return redirect('empresa index')

@login_required(login_url="empresa login")
def deletar_vaga(request):
    id_vaga = request.POST.get('id_vaga')
    vaga = Vaga.objects.get(id_vaga = id_vaga)
    vaga.delete()
    return redirect('empresa index')

@login_required(login_url="empresa login")
def editar_vaga(request):
    id_vaga = request.POST.get('id_vaga')
    vaga = Vaga.objects.get(id_vaga = id_vaga)
    context = {
        'editar': True,
        'vaga': vaga
    }
    return render(request, 'empresa_vaga.html', context)

def editar_vaga2(request):
    vaga = Vaga(
        id_vaga = request.POST.get('id_vaga'),
        nome = request.POST.get('nome'),
        faixa_salarial = request.POST.get('faixa_salarial'),
        escolaridade = request.POST.get('escolaridade'),
        nome_da_empresa = request.user.first_name,
        email_da_empresa = request.user.username
    )
    vaga.save()
    return redirect('empresa index')