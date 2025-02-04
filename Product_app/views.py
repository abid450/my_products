from django.shortcuts import render, HttpResponse
from django.views.generic import View,CreateView,FormView,TemplateView
from .forms import *
from .models import *
# Create your views here.

class Product(FormView):
    template_name = 'sale.html'
    form_class = product_contact

    def form_valid(self, form):
        form.save()
        return HttpResponse('<h2>Submited form Successfully</h2>')