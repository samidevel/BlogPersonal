import datetime
#
from django.shortcuts import render
#from django.contrib.auth.mixins import LoginRequiredMixin
#from django.urls import reverse_lazy, reverse

#app entrada
from applications.entrada.models import Entry
#models
from .models import Home
#form
from .forms import SubscribersForm, ContactForm


from django.views.generic import (
    TemplateView,
    CreateView,
)

class HomePageView(TemplateView):
    template_name = "home/index.html"
   

    def get_context_data(self, **kwargs):   
        context = super(HomePageView, self).get_context_data(**kwargs)
         #cargamos el home
        context["home"] = Home.objects.latest('create_date')
        #contexto apra la portada
        context["portada"] = Entry.objects.entrada_en_portada()
        #contexto para los articulos en home
        context["entradas_home"] = Entry.objects.entradas_en_home()
        #entradas recientes
        context["entradas_recientes"] = Entry.objects.entradas_recientes()
        #enviamos formulario de subscripcion
        context["form"] = SubscribersForm
        
        return context


class SubscriberCreateView(CreateView):
    form_class = SubscribersForm
    success_url = '.'
 
    
    
    
class ContactCreateView(CreateView):
    form_class = ContactForm
    success_url = '.'
 



    
    
    
