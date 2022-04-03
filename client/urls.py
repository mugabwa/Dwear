from django.urls import path
from django.contrib.auth import views as auth_views
from .views import create_user, LoginUser


urlpatterns = [
    path('register/',create_user,name='register-user'),
    path('', LoginUser.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout_user.html'), name='logout-user'),
]
