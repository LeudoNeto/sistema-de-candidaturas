from django.shortcuts import redirect, render
from django.contrib.auth import logout as django_logout

# Create your views here.
def index(request):
    context = {'lista' : ['oi', 'bom dia']}
    return render(request, 'index.html', context)

def logout(request):
    django_logout(request)
    return redirect('index')

def mudar_grupo(request):
    if str(request.user.groups.all()[0]) == 'empresas':
        django_logout(request)
        return redirect('candidato login')
    else:
        django_logout(request)
        return redirect('empresa login')