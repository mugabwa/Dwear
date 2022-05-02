from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (create_user, LoginUser, UserList, enable_user, disable_user,
        make_user_admin, remove_admin_user)


urlpatterns = [
    path('register/',create_user,name='register-user'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout_user.html'), name='logout-user'),
    path('', UserList.as_view(), name='user-list'),
    path('<int:pk>/enable/', enable_user, name='user-enable'),
    path('<int:pk>/disable/', disable_user, name='user-disable'),
    path('<int:pk>/add_admin', make_user_admin, name='user-admin'),
    path('<int:pk>/remove_admin', remove_admin_user, name='user-not-admin'),
]
