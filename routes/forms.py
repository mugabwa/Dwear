from django import forms
from .models import Route


class FileForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ["filepath",]

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ["origin", "destination", "distance", "condition", "cost"]
        widgets = {
            'origin': forms.TextInput(attrs={'class': 'form-control p-input'}),
            'destination': forms.TextInput(attrs={'class': 'form-control p-input'}),
            'distance': forms.TextInput(attrs={'class': 'form-control p-input'}),
            'cost': forms.TextInput(attrs={'class': 'form-control p-input'}),
        }
