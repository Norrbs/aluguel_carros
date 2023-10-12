from django.shortcuts import render, redirect
from .models import Carro
from .forms import CarroForm
from django.contrib import messages

# Create your views here.

def home(request):
  return render(request, 'home.html')

def listar(request):
  carros = Carro.objects.all().order_by('modelo')
  return render(request, 'listar.html',{'carros':carros})

def detalhar(request,id):
  carro = Carro.objects.get(id=id)
  return render(request, 'detalhar.html',{'carro':carro})

def adicionar(request):
  if request.method == 'POST':
    form = CarroForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      messages.add_message(request, messages.SUCCESS, "Carro adicionado com sucesso!")
      return redirect('listar')
  else:
    form = CarroForm()
    return render(request, 'adicionar.html',{'form':form})
  
def atualizar(request,id):
  carro = Carro.objects.get(id=id)
  form = CarroForm(instance=carro)
  if request.method == 'POST':
    form = CarroForm(request.POST, request.FILES, instance=carro)
    if form.is_valid():
      form.save()
      messages.add_message(request, messages.INFO, "Informações do carro foram atualizadas")
      return redirect('listar')
    else:
      return render(request, 'atualizar.html', {'form':form})
  else:
    return render(request, 'atualizar.html', {'form':form})
  
def deletar(request,id):
  carro = Carro.objects.get(id=id)
  carro.delete()
  messages.add_message(request, messages.INFO, "Carro removido")
  return redirect('listar')

