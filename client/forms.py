from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser

class UserForm(forms.ModelForm):
    class Meta:
        FORM_CONTOL = 'form-control'
        model = CustomUser
        fields = ["email", "first_name", "last_name", "password", "is_staff"]

        widgets = {
            'email': forms.TextInput(attrs={'class': FORM_CONTOL, 'type': 'email'}),
            'first_name': forms.TextInput(attrs={'class': FORM_CONTOL, 'type': 'text'}),
            'last_name': forms.TextInput(attrs={'class': FORM_CONTOL, 'type': 'text'}),
            'password': forms.TextInput(attrs={'class': FORM_CONTOL, 'type': 'password'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("email is already taken")
        return email

    def clean(self):
        return super().clean()

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control'}
        )