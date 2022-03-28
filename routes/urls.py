from django.urls import path
from .views import RouteListView, RouteUpdate, update

urlpatterns = [
    path('routes/',RouteListView.as_view(), name='route-list'),
    path('routes/<int:pk>/update', update, name='route-update'),
]