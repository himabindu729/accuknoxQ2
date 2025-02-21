from django.db import models
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
# Create your models here.

class MainModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MainModel)
def signal_handler(sender, instance, **kwargs):
    print(f"[Signal] Running in thread: {threading.current_thread().name}")
