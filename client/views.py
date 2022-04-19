from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import views as auth_views

from .forms import UserForm, LoginForm

def create_user(request):
    if request.user.is_authenticated:
        return redirect('route-list')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            login(request, user)
            return redirect('route-list')
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})

class LoginUser(auth_views.LoginView):
    template_name='login_user.html'
    redirect_authenticated_user=True
    authentication_form = LoginForm