from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.shortcuts import render , redirect

from .forms import RouteForm
from .models import Route


class RouteListView(ListView):
    model = Route
    template_name = 'route_list.html'
    context_object_name = 'routes'


class RouteUpdate(UpdateView):
    model = Route
    fields = ['origin', 'destination', 'distance', 'cost']
    template_name = 'route_update_form.html'
    context_object_name = 'route'

    def get_success_url(self):
        return reverse('route-list')


def update(request, pk=None):
    route = Route.objects.get(id=pk)
    form = RouteForm(instance=route)
    if request.method == 'POST':
        form = RouteForm(request.POST, instance=route)
        if form.is_valid():
            form.save()
            return redirect("route-list")
        else:
            return render(request, 'route_update_form.html')
    context = {
        "form": form,
        "route": route
    }
    return render(request, 'route_update_form.html', context)
