
from django.contrib import admin
from django.urls import path, include
from .views import fcliente, salvar, excluir


urlpatterns = [
    path('', fcliente),
    path('salvar/', salvar, name='salvar'),
    path('excluir/<int:id>', excluir, name='excluir'),

]
