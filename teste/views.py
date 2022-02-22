from django.shortcuts import render
from django.http import HttpResponse





# Create your views here.
def nome(request):
    return HttpResponse('Nome, E-mail, Senha')  

def email(request):
    return HttpResponse('email')

def senha(request): 
    return HttpResponse('Senha')
    