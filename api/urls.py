from django.urls import path
from .views import fetchData, loadData, login_user, register_user, sendData

urlpatterns = [
    path('load_data/', loadData),
    path('fetch_data/',fetchData),
    path('send_data/',sendData),
    path('register_user/',register_user),
    path('login_user/', login_user),
]