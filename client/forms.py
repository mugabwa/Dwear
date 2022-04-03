from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser

class UserForm(forms.ModelForm):
    class Meta:
        FORM_CONTOL = 'form-control'
        model = CustomUser
        fields = ["email", "password"]

        widgets = {
            'email': forms.TextInput(attrs={'class': FORM_CONTOL, 'type': 'email'}),
            'password': forms.TextInput(attrs={'class': FORM_CONTOL, 'type': 'password'}),
        }


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control'}
        )