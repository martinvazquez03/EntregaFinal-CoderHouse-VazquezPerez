from django.shortcuts import render

# Create your views here.

def view_Producto(request):
    return render(request, "Producto/index.html")