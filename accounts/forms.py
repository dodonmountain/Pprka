from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'last_name', 'first_name', 'phone_number', 'email')
        labels = {
            'phone_number': '휴대폰'
        }
        widgets = {
            'phone_number': forms.TextInput(
                attrs={
                    'placeholder': "'-' 없이 입력해주세요"
                }
            )
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('last_name', 'first_name', 'phone_number', 'email')
        labels = {
            'phone_number': '휴대폰'
        }
        widgets = {
            'phone_number': forms.TextInput(
                attrs={
                    'placeholder': "'-' 없이 입력해주세요"
                }
            )
        }