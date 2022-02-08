from django.urls import path
from .views import fetchData, loadData, stopData

urlpatterns = [
    path('load_data/', loadData),
    path('fetch_data/',fetchData),
    path('stop_data/',stopData),
]