from django.urls import path
from .views import (RouteListView, update, create_route,
        plot_graph, delete_route, recalculate_cost)
urlpatterns = [
    path('routes/',RouteListView.as_view(), name='route-list'),
    path('routes/<int:pk>/update/', update, name='route-update'),
    path('routes/create/',create_route, name='route-create'),
    path('routes/<int:pk>/graph/', plot_graph, name='route-graph'),
    path('routes/<int:pk>/delete/', delete_route, name='route-delete'),
    path('routes/<int:pk>/recalculate_cost/', recalculate_cost, name='recalculate-cost'),
]