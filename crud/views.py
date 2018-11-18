from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from .models import Member
from django.db.models import Q


def index_redirect(request):
    return  redirect('/crud/')
     
def index(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'crud/index.html', context)
 
def create(request):
    member = Member(Nombre=request.POST['Nombre'], Apellido=request.POST['Apellido'],DNI=request.POST['DNI'], Fechanac=request.POST['Fechanac'])
    member.save()
    return redirect('/')
 
def edit(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'crud/edit.html', context)
 
def update(request, id):
    member = Member.objects.get(id=id)
    member.Nombre = request.POST['Nombre']
    member.Apellido = request.POST['Apellido']
    member.DNI = request.POST['DNI']
    member.Fechanac = request.POST['Fechanac']
    member.save()
    return redirect('/crud/')
 
def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('/crud/')


def search(request):
    members = Member.objects.filter(Q(DNI=request.GET.get('search')))
    return render(request, 'crud/index.html' , {'members': members}) 
