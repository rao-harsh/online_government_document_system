from django import forms
from . import models

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class IncomeForm(forms.ModelForm):
    class Meta:
        model = models.Income
        fields = ("__all__")

class NonCreamyLayerForm(forms.ModelForm):
    class Meta:
        model = models.Non_Creamy_Layer
        fields = ("__all__")
