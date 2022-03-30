from django.urls import path
from .views import fetchData, loadData, login_user, register_user, stopData, sendData

urlpatterns = [
    path('load_data/', loadData),
    path('fetch_data/',fetchData),
    path('stop_data/',stopData),
    path('send_data/',sendData),
    path('register_user/',register_user),
    path('login_user/', login_user),
]