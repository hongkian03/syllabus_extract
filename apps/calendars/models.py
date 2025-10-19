from django.db import models
from apps.syllabus.models import ExtractedEvent

# Calendar Event
class CalendarEvent(models.Model):

    # link to the extracted event
    extracted_event = models.ForeignKey(
        ExtractedEvent,
        on_delete=models.CASCADE,
        related_name="calendar_event"
    )

    # calendar event details
    provider = models.CharField(max_length=50)  # e.g., "Google Calendar", "Outlook"
    external_id = models.CharField(max_length=255)  # ID from the external calendar for our own use when tracking/updating

    # sync status
    SYNC_STATUS_CHOICES = [
        ("pending", "Pending"),
        ("synced", "Synced"),
        ("failed", "Failed"),
    ]
    sync_status = models.CharField(max_length=20, choices=SYNC_STATUS_CHOICES, default="pending")
    last_sync_at = models.DateTimeField(blank=True, null=True)  # this will reflect both last created and last updated
    error_msg = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"CalendarEvent {self.id} - {self.title} on {self.date}"