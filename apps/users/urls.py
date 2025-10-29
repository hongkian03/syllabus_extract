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

    # settings path
    path("settings/", views.settings_view, name="settings"),

    # change username paths
    path("settings/username/", views.change_username_view, name="change_username"),
    path("settings/username/done", views.change_username_done, name="change_username_done"),

    # change email paths
    path("settings/email/", views.change_email_view, name="change_email"),
    path("settings/email/done", views.change_email_done, name="change_email_done"),

    # update API key paths
    path("settings/api-key/", views.update_api_key_view, name="update_api_key"),
    path("settings/api-key/done", views.update_api_key_done, name="update_api_key_done"),

     # change password paths
    path("settings/password-change", 
         auth_views.PasswordChangeView.as_view(template_name="users/password_change.html"), 
         name="change_password"),
    path("settings/password-change/done", 
         auth_views.PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"), 
         name="password_change_done"),
]