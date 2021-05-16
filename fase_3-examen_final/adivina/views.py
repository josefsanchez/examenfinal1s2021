from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def adivina_view (request):
        return render(request, 'adivina.html')


