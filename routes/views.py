import os
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render , redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .process_data import cost_data
from .read_file_data import read_data
from .forms import RouteForm, FileForm
from .models import Route


class RouteListView(LoginRequiredMixin, ListView):
    model = Route
    template_name = 'route_list.html'
    context_object_name = 'routes'


class RouteUpdate(LoginRequiredMixin, UpdateView):
    model = Route
    fields = ['origin', 'destination', 'distance', 'cost']
    template_name = 'route_update_form.html'
    context_object_name = 'route'

    def get_success_url(self):
        return reverse('route-list')

@login_required
@csrf_exempt
def update(request, pk=None):
    route = Route.objects.get(id=pk)
    form = RouteForm(instance=route)
    form1 = FileForm(instance=route)
    if request.method == 'POST':
        form = RouteForm(request.POST, instance=route)
        form1 = FileForm(request.POST, request.FILES, instance=route)
        if form.is_valid():
            form.save()
            return redirect("route-list")
        elif form1.is_valid():
            form1.save()
            calculate_cost(pk)
            return redirect('route-list')
        else:
            return render(request, 'route_update_form.html')
    context = {
        "form": form,
        "route": route,
        "form1": form1,
    }
    return render(request, 'route_update_form.html', context)


def calculate_cost(pk):
    route = Route.objects.get(id=pk)
    cost = cost_data(str(route.filepath))
    route.calculated_cost = cost
    route.cost_status = True
    route.save()

@login_required
def create_route(request):
    context = {}
    form = RouteForm(request.POST or None)
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('route-list')
    context = {
        'form': form,
    }
    return render(request, 'create_route.html', context)

@login_required
def plot_graph(request, pk):
    route = Route.objects.get(id=pk)
    data_path = route.filepath
    cur_dir = os.getcwd()
    cur_dir += "/media/"
    data_file = os.path.join(cur_dir, str(data_path))
    data = read_data(data_file,[2]).flatten()
    return render(request, 'graph_data.html', {'data': data.tolist(), 'data_len': len(data)})