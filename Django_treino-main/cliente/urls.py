
from django.contrib import admin
from django.urls import path, include
from .views import fcliente, salvar, excluir, update, editar


urlpatterns = [
    path('fcliente/', fcliente, name='fcliente'),
    path('salvar/', salvar, name='salvar'),
    path('excluir/<int:id>', excluir, name='excluir'),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),

]


