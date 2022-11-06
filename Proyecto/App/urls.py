from django.urls import path
from App.views import mostrar_familia

urlpatterns = [
    path('familia/', mostrar_familia)
]