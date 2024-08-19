from django.urls import path
from .views import IndexView
from .views import about, contactus, mayores, menores, vehiculos

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', about, name='about'),
    path('contactus/',contactus, name='contactus'),
    path('mayores/', mayores, name='mayores'),
    path('menores/', menores, name='menores'),
    path('vehiculos/', vehiculos, name='vehiculos'),
    
]
