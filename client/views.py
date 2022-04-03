from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import UserForm

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.changed_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('route-list')
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})