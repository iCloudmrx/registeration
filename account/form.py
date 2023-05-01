from django import forms


class LoginForm(forms.Form):
    username = forms.ChoiceField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
