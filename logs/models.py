from django.db import models
from django.conf import settings
import uuid


# Create your models here.
class LogCollection(models.Model):
    unique_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    create_time = models.DateTimeField()


class Log(models.Model):
    collection = models.ForeignKey(LogCollection, on_delete=models.CASCADE)
    log_text = models.TextField()
    ip_addr = models.GenericIPAddressField()
    received_time = models.DateTimeField()
