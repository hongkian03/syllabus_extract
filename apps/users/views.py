from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required

# signup view
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("signup_done")
    else:
        form = SignUpForm()
    return render(request, "users/signup.html", {"form": form})

# signup done view
def signup_done(request):
    return render(request, "users/signup_done.html")

# settings view
@login_required(login_url="/users/login/")
def settings_view(request):
    return render(request, "users/settings.html")

# change username view
@login_required(login_url="/users/login/")
def change_username_view(request):
    if request.method == 'POST':
        form = ChangeUsernameForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            return redirect("change_username_done")
    else:
        form = ChangeUsernameForm(instance=request.user)
    return render(request, "users/change_username.html", {"form": form})

# change username done view
def change_username_done(request):
    return render(request, "users/change_username_done.html")

# change email view
@login_required(login_url="/users/login/")
def change_email_view(request):
    if request.method == 'POST':
        form = ChangeEmailForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            return redirect("change_email_done")
    else:
        form = ChangeEmailForm(instance=request.user)
    return render(request, "users/change_email.html", {"form": form})

# change email done view
def change_email_done(request):
    return render(request, "users/change_email_done.html")

# update API key view
@login_required(login_url="/users/login/")
def update_api_key_view(request):
    if request.method == 'POST':
        form = UpdateAPIKeyForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            return redirect("update_api_key_done")
    else:
        form = UpdateAPIKeyForm(instance=request.user)
    return render(request, "users/update_api_key.html", {"form": form})

# update API key done view
def update_api_key_done(request):
    return render(request, "users/update_api_key_done.html")

# Note: we will use PasswordChangeView, PasswordChangeDoneView,
# LoginView, and LogoutView provided by Django