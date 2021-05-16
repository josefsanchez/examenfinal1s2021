"""
    Archivo de vistas del proyecto
"""


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def homepage (request):
        return render(request,'principal.html')


def adivina (request):
        return render(request, 'adivina.html')