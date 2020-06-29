from django.db import models
from django.conf import settings


# Create your models here.
class LogCollection(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    create_time = models.DateTimeField()


class Log(models.Model):
    collection = models.ForeignKey(LogCollection, on_delete=models.CASCADE)
    log_text = models.TextField()
    ip_addr = models.GenericIPAddressField()
    received_time = models.DateTimeField()
