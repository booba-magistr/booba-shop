from typing import Any
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, FormView, TemplateView, ListView, UpdateView
from .models import Stuff, Contact


class Index(ListView):
    model = Contact
    template_name = "main/home.html"
    context_object_name = "info"
    extra_context = {"title": 'Главная'}


class StuffView(ListView):
    model = Stuff
    context_object_name = 'stuff'
    template_name = "main/about.html"
    extra_context = {'title': 'Персонал'}


class ContactView(ListView):
    model = Contact
    context_object_name = 'contact'
    template_name = "main/contact_data.html"
    extra_context = {'title': 'Информация'}
    
    