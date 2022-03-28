from django import forms
from routes.models import RouteData
from .models import Route


class FileForm(forms.ModelForm):
    class Meta:
        model = RouteData
        fields = ['route', 'filepath']


class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = "__all__"
        widgets = {
            'origin': forms.TextInput(attrs={'class': 'form-control p-input'}),
            'destination': forms.TextInput(attrs={'class': 'form-control p-input'}),
            'distance': forms.TextInput(attrs={'class': 'form-control p-input'}),
            'cost': forms.TextInput(attrs={'class': 'form-control p-input'}),
        }
