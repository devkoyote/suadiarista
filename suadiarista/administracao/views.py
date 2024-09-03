from django.shortcuts import render
from .forms import ServicoForm

# Create your views here.
def cadastrar_servico(request):
    # validate method 
    if request.method == "POST":
        form_servico = ServicoForm(request.POST)
        if form_servico.is_valid():
            form_servico.save()
    else:
        form_servico = ServicoForm()
    return render(request, 'servicos/form_servico.html', {"form_servico": form_servico})
