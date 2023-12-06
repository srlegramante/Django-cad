from django.shortcuts import render
from .models import Usuarios

# Create your views here.
def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    novo_usuarios = Usuarios()
    novo_usuarios.nome = request.POST.get('nome')
    novo_usuarios.idade = request.POST.get('idade')
    novo_usuarios.save()
    # exibir todos os usuarios ja cadastrados em uma nova pagina
    usuarios = {
        'usuarios': Usuarios.objects.all()
    }
    #retornar os dados para a pagina de listagem dos usuarios
    return render(request,'usuarios/usuarios.html', usuarios)