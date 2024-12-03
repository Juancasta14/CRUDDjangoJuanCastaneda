from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from .forms import LibroForm

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/lista_libros.html', {'libros': libros})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'libros/crear_libro.html', {'form': form})

def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/editar_libro.html', {'form': form})

def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')
    return render(request, 'libros/eliminar_libro.html', {'libro': libro})

def lista_libros(request):
    query = request.GET.get('q')  # Obtiene el término de búsqueda de la URL
    if query:
        libros = Libro.objects.filter(titulo__icontains=query)  # Filtra por título
    else:
        libros = Libro.objects.all()
    return render(request, 'libros/lista_libros.html', {'libros': libros})