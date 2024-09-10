from django.shortcuts import redirect, render
from .forms import ServicoForm
from .models import Servico

# Create your views here.
def cadastrar_servico(request):
    # validate method 
    if request.method == "POST":
        form_servico = ServicoForm(request.POST)
        if form_servico.is_valid():
            form_servico.save()
            return redirect('listar_servicos')
    else:
        form_servico = ServicoForm()
    return render(request, 'servicos/form_servico.html', {"form_servico": form_servico})

def listar_servico(request):
    # Consult all datas
    servicos = Servico.objects.all()
    return render(request, 'servicos/lista_servico.html', {'servicos': servicos})

def editar_servico(request, id):
    # capture object first
    servico = Servico.objects.get(id=id)
    form_servico = ServicoForm(request.POST or None, instance=servico)
    # validate [datas]
    if form_servico.is_valid():
        form_servico.save()
        #redirect for list
        return redirect('listar_servicos')
    # return form_servicos [datas]
    return render(request, 'servicos/form_servico.html', {'form_servico': form_servico})

