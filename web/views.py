from django.views import View
from django.shortcuts import render

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')
    

class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')
