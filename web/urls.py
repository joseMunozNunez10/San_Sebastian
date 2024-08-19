from django.urls import path
from .views import IndexView
from .views import about

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', about, name='about'),
]
