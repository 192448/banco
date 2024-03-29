from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.views import View
from .models import Cuenta

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# create engine
engine = create_engine('postgres://banco_db_user:OLvdylM6qfzalR8JJQeK922XePTqbQSh@dpg-cn0shcla73kc73edas8g-a.oregon-postgres.render.com/banco_db')

"""
with Session(engine) as session:
        #return dictionary containing the serialized data of all videogames
        return serialize_raw_query_data(session.execute(text(SELECT)))
"""

# Create your views here.
class CuentaList(ListView):
    model = Cuenta
    template_name = 'list.html'

def CuentaDeposito(request):
    if request.method == 'GET': 
        return render(request, 'deposito.html')
    
    elif request.method == 'POST':
        cuenta = Cuenta.objects.get(id=request.POST.get('cuenta'))
        cuenta.saldo = cuenta.saldo + int(request.POST.get('cantidad'))
        cuenta.save()
        return HttpResponseRedirect('/')

def CuentaRetiro(request):
    if request.method == 'GET': 
        return render(request, 'retiro.html')
    
    elif request.method == 'POST':
        cuenta = Cuenta.objects.get(id=request.POST.get('cuenta'))
        if int(request.POST.get('cantidad')) > cuenta.saldo:
            return HttpResponseRedirect('/')
        cuenta.saldo = cuenta.saldo - int(request.POST.get('cantidad'))
        cuenta.save()
        return HttpResponseRedirect('/')

def CuentaTransferencia(request):
    if request.method == 'GET': 
        return render(request, 'transferir.html')
    
    elif request.method == 'POST':
        cuentaO = Cuenta.objects.get(id=request.POST.get('cuentaO'))
        cuentaD = Cuenta.objects.get(id=request.POST.get('cuentaD'))
        if int(request.POST.get('cantidad')) > cuentaO.saldo:
            return "<h1>No se cuenta con esa cantidad de dinero</h1>"
        cuentaO.saldo = cuentaO.saldo - int(request.POST.get('cantidad'))
        cuentaD.saldo = cuentaD.saldo + int(request.POST.get('cantidad'))
        cuentaO.save()
        cuentaD.save()
        return HttpResponseRedirect('/')
