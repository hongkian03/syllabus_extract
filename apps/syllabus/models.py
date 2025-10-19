from django.db import models
from django.conf import settings

# Syllabus Upload
class SyllabusUpload(models.Model):

    # each upload is linked to a user
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="syllabus_uploads"
    )

    # file field to store the uploaded syllabus
    file = models.FileField(upload_to="syllabus_uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # status tracking
    STATUS_CHOICES = [
        ("uploaded", "Uploaded"),
        ("parsed", "Parsed"),
        ("error", "Error"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="uploaded")
    error_msg = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"SyllabusUpload {self.id} by {self.user.username} - {self.status}"
    
# Extracted Event
class ExtractedEvent(models.Model):

    # link to the syllabus upload
    syllabus = models.ForeignKey(
        SyllabusUpload,
        on_delete=models.CASCADE,
        related_name="events"
    )

    # event type
    EVENT_TYPE_CHOICES = [
        ("assignment", "Assignment"),
        ("exam", "Exam"),
    ]
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES)

    # event details
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    course = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ExtractedEvent {self.id} - {self.title} on {self.date}"