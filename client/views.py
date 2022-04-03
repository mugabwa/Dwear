from django.shortcuts import render

from .forms import UserForm

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})