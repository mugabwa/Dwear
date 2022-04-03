from django import forms
from .models import CustomUser

class UserForm(forms.ModelForm):
    class Meta:
        FORM_CONTOL = 'form-control p-input'
        model = CustomUser
        fields = "__all__"
