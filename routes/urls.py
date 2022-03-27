from django.urls import path
from .views import RouteListView, RouteUpdate

urlpatterns = [
    path('routes/',RouteListView.as_view(), name='route-list'),
    path('routes/<int:pk>/update', RouteUpdate.as_view(), name='route-update'),
]