from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.shortcuts import render
from .models import Route


class RouteListView(ListView):
    model = Route
    template_name = 'route_list.html'
    context_object_name = 'routes'


class RouteUpdate(UpdateView):
    model = Route
    fields = ['origin','destination','distance','condition','cost']
    template_name = 'route_update_form.html'
    context_object_name = 'route'