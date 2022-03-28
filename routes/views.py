
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from .models import Route


class RouteListView(ListView):
    model = Route
    template_name = 'route_list.html'
    context_object_name = 'routes'


class RouteUpdate(UpdateView):
    model = Route
    fields = ['origin','destination','distance','cost']
    template_name = 'route_update_form.html'
    context_object_name = 'route'

    def get_success_url(self):
        return reverse('route-list')