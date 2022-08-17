from django.shortcuts import redirect, render
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth.decorators import login_required
from candidato.models import Candidatura

from empresa.models import Vaga

# Create your views here.
@login_required(login_url="candidato login")
def index(request):
    user = request.user
    if str(user.groups.all()[0]) == 'empresas':
        return redirect('empresa index')

    vagas_disponiveis = list(Vaga.objects.all())

    escolaridades = ['Ensino fundamental', 'Ensino médio', 'Tecnólogo', 'Ensino Superior', 'Pós / MBA / Mestrado', 'Doutorado']
    faixas_salariais = ['Até 1.000', 'De 1.000 a 2.000', 'De 2.000 a 3.000', 'Acima de 3.000']

    for vaga in vagas_disponiveis:
        vaga.escolaridade_original = escolaridades[vaga.escolaridade - 1]
        vaga.faixa_salarial_original = faixas_salariais[vaga.faixa_salarial - 1]

    candidaturas = Candidatura.objects.filter(email_do_candidato = user.username).all()
    vagas_candidatadas = []
    for candidatura in candidaturas:
        vaga_candidatada = Vaga.objects.get(id_vaga = candidatura.id_vaga)

        vaga_candidatada.escolaridade_original = escolaridades[vaga.escolaridade - 1]
        vaga_candidatada.faixa_salarial_original = faixas_salariais[vaga.faixa_salarial - 1]

        vagas_candidatadas.append(vaga_candidatada)
        vagas_disponiveis.remove(vaga_candidatada)

    if len(vagas_disponiveis) > 0:
        vaga1 = True
    else:
        vaga1 = False

    if len(vagas_candidatadas) > 0:
        candidatura1 = True
    else:
        candidatura1 = False

    context = {
        'vaga1' : vaga1,
        'candidatura1' : candidatura1,
        'nome': user.first_name,
        'vagas_disponiveis': vagas_disponiveis,
        'candidaturas': vagas_candidatadas
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
            if str(user.groups.all()[0]) == 'empresas':
                context = {
                    'empresa': True
                }
                return render(request, 'candidato_login.html', context)
            else:
                django_login(request, user)
                return redirect('candidato index')
        else:
            context = {
                'invalid': True
            }
            return render(request, 'candidato_login.html', context)

@login_required(login_url="candidato login")
def inscricao(request):
    id_vaga = request.GET.get('id_vaga')
    context = {
        'nome': request.user.first_name,
        'vaga': Vaga.objects.filter(id_vaga = id_vaga).first()
    }
    return render(request, 'candidato_inscricao.html', context)

@login_required(login_url="candidato login")
def realizar_inscricao(request):
    user = request.user
    id_vaga = request.POST.get('id_vaga')
    print(id_vaga)
    vaga = Vaga.objects.filter(id_vaga = id_vaga).first()
    
    candidatura = Candidatura(
        id_vaga = id_vaga,
        nome_da_empresa = vaga.nome_da_empresa,
        nome_da_vaga = vaga.nome,
        nome_do_candidato = user.first_name,
        email_do_candidato = user.username,
        pretensao_salarial = request.POST.get('pretensao_salarial'),
        experiencia = request.POST.get('experiencia'),
        escolaridade = request.POST.get('escolaridade')
    )

    candidatura.save()
    return redirect('candidato index')

@login_required(login_url="candidato login")
def cancelar_inscricao(request):
    user = request.user
    id_vaga = request.POST.get('id_vaga')

    Candidatura.objects.get(id_vaga = id_vaga, email_do_candidato = user.username).delete()
    return redirect('candidato index')