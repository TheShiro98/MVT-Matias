from django.shortcuts import render
from App.models import Familias
# Create your views here.

def mostrar_familia(request):

    f1 = Familias(nombre = 'Lisandro', apellido = 'Martinez', edad = 23, nacimiento = '1999-10-27')
    f2 = Familias(nombre = 'Dibu', apellido = 'Martinez', edad = 25, nacimiento = '1997-09-03')
    f3 = Familias(nombre = 'Lautaro', apellido = 'Martinez', edad = 21, nacimiento = '2002-06-08')

    f4 = Familias(nombre = 'Leo', apellido = 'Messi', edad = 35, nacimiento = '1987-06-08')
    f5 = Familias(nombre = 'Ciro', apellido = 'Messi', edad = 4, nacimiento = '2018-06-08')
    f6 = Familias(nombre = 'Mateo', apellido = 'Messi', edad = 7, nacimiento = '2015-06-08')

    f7 = Familias(nombre = 'Matth', apellido = 'Álvarez', edad = 15, nacimiento = '2006-09-18')
    f8 = Familias(nombre = 'Pedro', apellido = 'Álvarez', edad = 24, nacimiento = '1998-05-17')
    f9 = Familias(nombre = 'Julián', apellido = 'Álvarez', edad = 22, nacimiento = '2000-01-31')
    return render(request,'familia.html',{'fam':[f1,f2,f3,f4,f5,f6,f7,f8,f9]})

