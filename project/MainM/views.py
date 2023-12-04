from django.shortcuts import render

# Create your views here.

def view_mainmenu(request):
    return render(request, "MainM/index.html")

def view_about(request):
    return render(request, "MainM/about.html")