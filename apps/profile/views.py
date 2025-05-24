from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from allauth.account.forms import AddEmailForm
from .forms import CustomChangePasswordForm, CustomChangeAvatarForm
from django.contrib import messages
from .models import CustomUser
from apps.services.models import Advertisement

@login_required
def profile(request, username=None):
    message = ''
    password_form = CustomChangePasswordForm(request.user)
    email_form = AddEmailForm(request.user)
    avatar_form = CustomChangeAvatarForm(instance=request.user)
    user = get_object_or_404(CustomUser, username=username)
    ads = Advertisement.objects.filter(owner=request.user).order_by('-created_at')
    if request.method == 'POST':
        if 'change_password' in request.POST:
            password_form = CustomChangePasswordForm(request.user, request.POST)
            if password_form.is_valid():
                password_form.save()
                message = "Пароль успішно змінено"
                return redirect('profile', username=request.user.username)
        elif 'add_email' in request.POST:
            email_form = AddEmailForm(request.user, request.POST)
            if email_form.is_valid():
                email_form.save()
                messages.success(request, "Email успішно додано")
                return redirect('profile', username=request.user.username)
        elif 'change_avatar' in request.POST:
            avatar_form = CustomChangeAvatarForm(request.POST, request.FILES, instance=request.user)
            if avatar_form is not None:
                avatar_form.save()
                messages.success(request, "Аватар успішно змінено")
                return redirect('profile', username=request.user.username)
    
    return render(request, 'profile.html', {
        'password_form': password_form,
        'email_form': email_form,
        'avatar_form': avatar_form,
        'message': message,
        'username': user,
        'ads': ads,
    })