from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Livro


def teste(request):
    template = loader.get_template('paginateste.html')
    return HttpResponse(template.render())

def principal(request):
    template = loader.get_template('principal.html')
    return HttpResponse(template.render())

def livros (request):
    context = {
        'livros': [
            {
                "nome": " A Metamorfose",
                "autor": "Franz Kafka",
                "ano": 1915
            }
        ]
    }

    template = loader.get_template('livros.html')
    return HttpResponse(template.render(context, request))