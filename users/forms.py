from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser
from django import forms

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")





class VerifyOTPForm(forms.Form):
    otp=forms.CharField(max_length=6)
