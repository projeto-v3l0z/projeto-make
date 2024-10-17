from django.urls import path
from .views import *

urlpatterns = [
    path('', FormularioView.as_view(), name='formulario'),
]