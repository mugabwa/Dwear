from django.urls import path
from .views import RouteListView, update, create_route


urlpatterns = [
    path('routes/',RouteListView.as_view(), name='route-list'),
    path('routes/<int:pk>/update/', update, name='route-update'),
    path('routes/create/',create_route, name='route-create'),
]