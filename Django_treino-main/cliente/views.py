from django.shortcuts import render

from .models import Cliente

from django.contrib import messages
# Create your views here.


from django.shortcuts import render, redirect

from .models import Cliente

from django.contrib import messages

# Create your views here.

def fcliente(request):
    clientes = Cliente.objects.all()
    return render(request,"frCliente.html",{"clientes":clientes})


def salvar(request):
    vnome = request.POST.get("nome")
    vtelefone = request.POST.get("telefone")
    vemail = request.POST.get("email")

    Cliente.objects.create(nome=vnome, telefone=vtelefone, email=vemail)
    return redirect('fcliente')



"""
def excluir(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    clientes = Cliente.objects.all()
    return render(request, "frCliente.html", {"clientes": clientes})
"""

def excluir(request, id):
    try:
        cliente = Cliente.objects.get(id=id)
        cliente.delete()
        return redirect('fcliente')
    except Cliente.DoesNotExist:
        messages.error(request, "Cliente não encontrado.")
        return redirect('fcliente')

def editar(request, id):
    cliente = Cliente.objects.get(id=id)
    return render(request, "update.html", {"cliente": cliente})


def update(request, id):
    vnome = request.POST.get("nome")
    vtelefone = request.POST.get("telefone")
    vemail = request.POST.get("email")
    cliente = Cliente.objects.get(id=id)
    cliente.nome = vnome
    cliente.telefone = vtelefone
    cliente.email = vemail
    cliente.save()

    return redirect('fcliente')