"""
    Pantalla de login
"""

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, redirect

def logon(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        usersession = authenticate(request, username = username, password= password)
        if usersession:
            login(request, usersession)
            return redirect("homepage")
        else:
            return render(request, 'index.html', {'error' : "Usuario o contraseña invalido"})
    return render(request,'index.html')

def logout_view(request):
    logout(request)
    return redirect("logon")