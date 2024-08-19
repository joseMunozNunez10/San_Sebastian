from django.views import View
from django.shortcuts import render

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')
    

def about(request):
    return render(request, 'about.html')

def contactus(request):
    return render(request, 'contactus.html')

def mayores(request):
    return render(request, 'mayores.html')

def menores(request):
    return render(request, 'menores.html')

def vehiculos(request):
    return render(request, 'vehiculos.html')
