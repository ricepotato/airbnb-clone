from django import forms
from django.forms import widgets
from . import models


class LoginForm(forms.Form):
    email = forms.EmailField(initial="ricepotato40@gmail.com")
    password = forms.CharField(widget=widgets.PasswordInput())

    """def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(username=email)
            return email
        except models.User.DoesNotExist:
            raise forms.ValidationError("User Does not exist")

    def clean_password(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(username=email)
            if user.check_password(password):
                return password
            else:
                raise forms.ValidationError("password wrong")
        except models.User.DoesNotExist:
            raise forms.ValidationError("User Does not exist")"""

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("password wrong"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User Does not exist"))
