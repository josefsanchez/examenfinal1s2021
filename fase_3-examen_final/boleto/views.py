"""
    Vistas de programa de boletos de aerolínea
"""
from boleto.forms import BoletoForm, TotalForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Boleto


def calcular (request):
    if request.method == "POST":
        clase = request.POST
        print (clase)
    
@login_required
def boleto_view (request):
        form1 = BoletoForm()
        form2 = TotalForm()
        st  = ""
        td  = ""
        tt  = ""
        b   = ""
        try:
            if request.method == "POST":
                form1 = BoletoForm(request.POST)
                
                if form1.is_valid():
                    clase = form1.cleaned_data.get("clase")
                    tc = form1.cleaned_data.get("comida")
                    tb = form1.cleaned_data.get("bebida")
                    tp = form1.cleaned_data.get("pelicula")
                    ts = tc+tb+tp
                    if clase == 1:
                        co = 50
                        be = 35
                        pe = 70
                    elif clase ==2:
                        co = 40
                        be = 25
                        pe = 55
                    elif clase ==3:
                        co = 25
                        be = 25
                        pe = 25
                    if clase == 1 and tc >=1 and tb>=1 and tp >=1:
                        d1 = 5
                    else:
                        d1 = 0
                    if ts >=10:
                        d2 = 10
                    else:
                        d2 = 0
                    td  = d1+d2
                    st  = tc*co + tb*be + tp*pe
                    tt  = st - (st*td/100)
                    b=  Boleto(subtotal=st, desc=td, total=tt)
                    b.save()
                    
                    #print (clase, tc,tb,tp,ts,st,d1,d2,td,tt)
                else:
                    print(form1.errors)
        except:
            form1 = BoletoForm()
            form2 = TotalForm()
            st  = ""
            td  = ""
            tt  = ""
            b   = ""  
        context={
            "formi": form1,
            "st":st,
            "td":td,
            "tt":tt
        }
        return render(request, 'boleto.html', context)


def reporte(request):
    queryset = Boleto.objects.all()
    #print(queryset)
   
    context = {
        "object_list" : queryset
    }
    return render(request, "reporte.html",context)
        

