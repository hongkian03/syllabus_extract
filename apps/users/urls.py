from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    # signup path
    path("signup/", views.signup_view, name="signup"),
    path("signup/done", views.signup_done, name="signup_done"),

    # login/logout paths
    path("login/",  auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # settings paths
    path("settings/", views.settings_view, name="settings"),
    path("settings/api-key/", views.update_api_key_view, name="update_api_key"),
    path("settings/password-change", 
         auth_views.PasswordChangeView.as_view(template_name="users/password_change.html"), 
         name="password_change"),
    path("settings/password-change/done", 
         auth_views.PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"), 
         name="password_change_done"),
]