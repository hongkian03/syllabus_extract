from django.db import models
from django.conf import settings
from fernet_fields import EncryptedCharField

# User Profile
class UserProfile(models.Model):

    # link to built-in User model
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    # extra fields
    api_key = EncryptedCharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile of {self.user.username}"