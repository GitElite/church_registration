from django import forms

class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    user_password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'autocomplete': 'off'}))
