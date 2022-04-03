from django import forms
from .models import CustomUser

class UserForm(forms.ModelForm):
    class Meta:
        FORM_CONTOL = 'form-control p-input'
        model = CustomUser
        fields = ["email", "password"]

        widgets = {
            'email': forms.TextInput(attrs={'class': FORM_CONTOL}),
            'password': forms.TextInput(attrs={'class': FORM_CONTOL}),
        }

