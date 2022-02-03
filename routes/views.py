from django.views.generic import ListView
from django.shortcuts import render
from .models import Route
# Create your views here.
class RouteListView(ListView):
    model = Route
    template_name = 'route_list.html'
    context_object_name = 'routes'