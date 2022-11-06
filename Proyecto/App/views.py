from django.shortcuts import render
from App.models import Familias
# Create your views here.

def mostrar_familia(request):

    f1 = Familias(nombre = 'Leo', apellido = 'Messi', edad = 23, nacimiento = '1999-10-27')
    f2 = Familias(nombre = 'Dibu', apellido = 'Martinez', edad = 25, nacimiento = '1997-09-03')

    return render(request,'familia.html',{'fam':[f1,f2]})