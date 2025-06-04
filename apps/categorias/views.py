from django.shortcuts import render, redirect, get_object_or_404

from .forms import ClienteForm
from .models import Categoria

# Create your views here.

def add_categoria(request):
    template_name = 'categorias/add_categoria.html'
    context = {}
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('categorias:list_categorias')
    form = ClienteForm()
    context['form'] = form
    return render(request, template_name, context)

def list_categorias(request):
    template_name = 'categorias/list_categorias.html'
    categorias = Cliente.objects.filter()
    context = {
        'categorias': categorias
    }
    return render(request, template_name, context)

def edit_categoria(request, id_categoria):
    template_name = 'categorias/add_categoria.html'
    context ={}
    categoria = get_object_or_404(Cliente, id=id_categoria)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categorias:list_categorias')
    form = ClienteForm(instance=categoria)
    context['form'] = form
    return render(request, template_name, context)

def delete_categoria(request, id_categoria):
    categoria = Cliente.objects.get(id=id_categoria)
    categoria.delete()
    return redirect('categorias:list_categorias')