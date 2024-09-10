#import class
from django.urls import path
#import views
from .views import *

#routes
urlpatterns = [
    # default 
    path('servicos/cadastrar', cadastrar_servico , name='cadastrar_servico'),
    path('servicos/listar', listar_servico, name='listar_servicos'),
    path('servicos/editar/<int:id>', editar_servico, name='editar_servico')
]