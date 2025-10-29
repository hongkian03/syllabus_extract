from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.users.utils import *
from validate_email import validate_email   # external library
from apps.users.utils import encrypt, is_valid_gemini_api_key
from apps.users.models import UserProfile


# Sign Up Form
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    api_key = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.PasswordInput(render_value=True),
        help_text="Your Gemini API key will be encrypted and stored securely."
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "api_key")

    # check email validity
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not validate_email(email):
            raise forms.ValidationError("Please enter a valid email address.")
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Email address already in use.")
        return email

    # check password validity
    def clean_password(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.") 


    # check API key validity
    def clean_api_key(self):
        api_key = self.cleaned_data.get("api_key")
        if api_key and not is_valid_gemini_api_key(api_key):
            raise forms.ValidationError("Invalid Gemini API key.")
        return api_key

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        api_key = self.cleaned_data.get("api_key")
        if api_key:
            profile, created = UserProfile.objects.get_or_create(user=user)
            profile.api_key = api_key
            profile.save()

        return user

    
# Update API Key Form
class UpdateAPIKeyForm(forms.ModelForm):
    api_key = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.PasswordInput(render_value=True),
        help_text="Your Gemini API key will be encrypted and stored securely."
    )

    class Meta:
        model = User
        fields = ("api_key",)

    # check API key validity
    def clean_api_key(self):
        api_key = self.cleaned_data.get("api_key")
        if api_key and not is_valid_gemini_api_key(api_key):
            raise forms.ValidationError("Invalid Gemini API key.")
        return api_key

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        api_key = self.cleaned_data.get("api_key")
        if api_key:
            profile, created = UserProfile.objects.get_or_create(user=user)
            profile.api_key = api_key
            profile.save()

        return user
    
# Change Username Form
class ChangeUsernameForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)

    class Meta:
        model = User
        fields = ("username",)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("Username already in use.")
        return username

# Change Email Form
class ChangeEmailForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("email",)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not validate_email(email):
            raise forms.ValidationError("Please enter a valid email address.")
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Email address already in use.")
        return email

# Update API Key Form
class UpdateAPIKeyForm(forms.ModelForm):
    api_key = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.PasswordInput(render_value=True),
        help_text="Your Gemini API key will be encrypted and stored securely."
    )

    class Meta:
        model = User
        fields = ("api_key",)

    # check API key validity
    def clean_api_key(self):
        api_key = self.cleaned_data.get("api_key")
        if api_key and not is_valid_gemini_api_key(api_key):
            raise forms.ValidationError("Invalid Gemini API key.")
        return api_key

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        api_key = self.cleaned_data.get("api_key")
        if api_key:
            profile, created = UserProfile.objects.get_or_create(user=user)
            profile.api_key = api_key
            profile.save()

        return user

# Note: we will use PasswordChangeForm for changing password
# and AuthenticationForm for login, which are provided by Django