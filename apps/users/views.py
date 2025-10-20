from django.shortcuts import render, redirect
from .forms import *

# signup view
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("profile")
    else:
        form = SignUpForm()
    return render(request, "users/signup.html", {"form": form})

# settings view
def settings_view(request):
    # TODO: Implement settings view (mainly just buttons to change passsword and update API key)
    pass

# update API key view
def update_api_key_view(request):
    # TODO: Implement update API key view
    pass

# Note: we will use PasswordChangeView, PasswordChangeDoneView,
# LoginView, and LogoutView provided by Django