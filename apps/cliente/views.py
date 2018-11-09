from django.shortcuts import render
from django.http import HttpResponse
from apps.cliente.forms import ClienteForm
# Create your views here.

def index_cliente(request):
	return render(request, 'cliente/index.html')

def formulario_view(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = ClienteForm()
    
    return render(request, 'cliente/index.html',{'form':form})
