from django import forms
from routes.models import RouteData

class FileForm(forms.ModelForm):
    class Meta:
        model=RouteData
        fields = ['route','filepath']

