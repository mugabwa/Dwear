from django.urls import path
from .views import fetchData, loadData, stopData, sendData, uploadFile

urlpatterns = [
    path('load_data/', loadData),
    path('fetch_data/',fetchData),
    path('stop_data/',stopData),
    path('send_data/',sendData),
    path('save_file/',uploadFile,name='save_file'),
]