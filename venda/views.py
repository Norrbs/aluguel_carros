from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'home.html')

def listar(request):
  return render(request, 'listar.html')