from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserForm, LoginForm
from .models import CustomUser

@login_required
def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('route-list')
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})

class LoginUser(auth_views.LoginView):
    template_name='login_user.html'
    redirect_authenticated_user=True
    authentication_form = LoginForm

class UserList(LoginRequiredMixin, ListView):
    template_name = 'list_users.html'
    model = CustomUser
    context_object_name = 'users'

@login_required
def enable_user(request, pk):
    if request.user.is_staff:
        user = CustomUser.objects.get(id=pk)
        user.is_active = True
        user.save()
    return redirect('user-list')

@login_required
def disable_user(request, pk):
    if request.user.is_staff:
        user = CustomUser.objects.get(id=pk)
        user.is_active = False
        user.save()
    return redirect('user-list')

@login_required
def make_user_admin(request, pk):
    if request.user.is_staff:
        user = CustomUser.objects.get(id=pk)
        user.is_staff = True
        user.save()
    return redirect('user-list')

@login_required
def remove_admin_user(request, pk):
    if request.user.is_staff:
        user = CustomUser.objects.get(id=pk)
        user.is_staff = False
        user.save()
    return redirect('user-list') 
