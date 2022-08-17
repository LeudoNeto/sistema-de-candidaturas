from django.shortcuts import redirect, render
from django.contrib.auth import logout as django_logout

# Create your views here.
def index(request):
    user = request.user
    if user.is_authenticated:
        if str(user.groups.all()[0]) == 'empresas':
            return redirect('empresa index')
        elif str(user.groups.all()[0]) == 'candidatos':
            return redirect('candidato index')

    return render(request, 'index.html')

def logout(request):
    django_logout(request)
    return redirect('index')