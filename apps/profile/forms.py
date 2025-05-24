from django import forms
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm, ChangePasswordForm
from .models import CustomUser

User = get_user_model()
 
class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=100, required=True, label='Ім\'я')
    last_name = forms.CharField(max_length=100, required=True, label='Прізвище')

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

class CustomChangePasswordForm(ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['oldpassword'].widget.attrs.update({
            'placeholder': 'Старий пароль',
            'class': 'form-control'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Новий пароль',
            'class': 'form-control'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Підтвердження пароля',
            'class': 'form-control'
        })

class CustomChangeAvatarForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['avatar']