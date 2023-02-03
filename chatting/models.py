from datetime import datetime, timezone

from django.db import models



class Sender(models.Model):
    name = models.CharField(max_length=225, blank=True, null=True)


class Message(models.Model):
    sender = models.ForeignKey('Sender', on_delete=models.CASCADE, blank=True, null=True, related_name='messages')
    timestamp = models.DateTimeField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.timestamp:
            self.timestamp = datetime.now(timezone.utc)
        super().save(*args, **kwargs)