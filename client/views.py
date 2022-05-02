from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .forms import UserForm, LoginForm

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