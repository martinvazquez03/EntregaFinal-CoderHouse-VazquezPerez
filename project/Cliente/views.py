from django.shortcuts import render

# Create your views here.

def view_Cliente(request):
    return render(request, "Cliente/index.html")