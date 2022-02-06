from django.urls import path
from .views import fetchData, loadData

urlpatterns = [
    path('load_data/', loadData),
    path('fetch_data/',fetchData),
]