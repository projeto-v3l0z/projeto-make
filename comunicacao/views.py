from django.shortcuts import render
from django.views.generic import FormView
from comunicacao.forms import FormularioTeste
from django.http import JsonResponse
import requests

# Create your views here.
class FormularioView(FormView):
    template_name = 'formulario.html'
    form_class = FormularioTeste
    success_url = '/'

    def form_valid(self, form):
        form_data = form.cleaned_data
        response = requests.post('https://hook.us2.make.com/efy3ek4j5wf79jv3ebfn4089cd2q6erk', data=form_data)
        print(response.text)
        return super().form_valid(form)