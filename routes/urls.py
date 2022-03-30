from django.urls import path
from .views import RouteListView, update, upload_file


urlpatterns = [
    path('routes/',RouteListView.as_view(), name='route-list'),
    path('routes/<int:pk>/update', update, name='route-update'),
    path('routes/<int:pk>/save_file/',upload_file,name='save-file'),
]