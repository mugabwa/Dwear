from django.urls import path
from .views import RouteListView, update, create_route, plot_graph


urlpatterns = [
    path('routes/',RouteListView.as_view(), name='route-list'),
    path('routes/<int:pk>/update/', update, name='route-update'),
    path('routes/create/',create_route, name='route-create'),
    path('routes/<int:pk>/graph/', plot_graph, name='route-graph'),
]