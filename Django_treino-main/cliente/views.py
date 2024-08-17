from django.shortcuts import render

from .models import Cliente
# Create your views here.


def fcliente(request):
    clientes = Cliente.objects.all()
    return render(request, "frCliente.html", {"clientes": clientes})


def salvar(request):
    vnome = request.POST.get("nome")
    vtelefone = request.POST.get("telefone")
    vemail = request.POST.get("email")

    Cliente.objects.create(nome=vnome, telefone=vtelefone, email=vemail)
    clientes = Cliente.objects.all()
    return render(request, "frCliente.html", {"clientes": clientes})


def excluir(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    clientes = Cliente.objects.all()
    return render(request, "frCliente.html", {"clientes": clientes})