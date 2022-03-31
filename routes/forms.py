from django import forms
from .models import Route


class FileForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ["filepath",]

class RouteForm(forms.ModelForm):
    class Meta:
        FORM_CONTOL = 'form-control p-input'
        model = Route
        fields = ["origin", "destination", "distance", "condition", "cost"]
        widgets = {
            'origin': forms.TextInput(attrs={'class': FORM_CONTOL}),
            'destination': forms.TextInput(attrs={'class': FORM_CONTOL}),
            'distance': forms.TextInput(attrs={'class': FORM_CONTOL}),
            'cost': forms.TextInput(attrs={'class': FORM_CONTOL}),
        }
