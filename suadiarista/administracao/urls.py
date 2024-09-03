#import class
from django.urls import path
#import views
from .views import *

#routes
urlpatterns = [
    # default 
    path('servicos/cadastrar', cadastrar_servico , name='cadastrar_servico'),
]