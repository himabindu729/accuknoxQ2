Do Django Signals Run in the Same Thread as the Caller?

Django provides a built-in signals framework that allows different parts of an application to communicate.
Yes, Django signals run in the same thread as the caller by default, meaning they execute synchronously. This means that when a signal is sent, Django waits for the corresponding signal handler to complete before executing the next line of code. The signal handler runs in the same thread as the function that triggered it.

Proof with a Code Snippet.The following code snippet demonstrates this behavior:

from django.db import models
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver

# Define a model
class MainModel(models.Model):
    name = models.CharField(max_length=100)

# Signal handler
@receiver(post_save, sender=MainModel)
def signal_handler(sender, instance, **kwargs):
    print(f"[Signal] Running in thread: {threading.current_thread().name}")

View to Test Signal Execution

from django.shortcuts import render, HttpResponse
import threading
from .models import MainModel

# View to trigger signal and print thread name
def test_signal_thread(request):
    print(f"[Caller] Running in thread: {threading.current_thread().name}")
    MainModel.objects.create(name="Test User")  
    return HttpResponse("Check the console for thread names.")

Expected Console Output:

When calling test_signal_thread, the console output will be:

[Caller] Running in thread: Thread-1
[Signal] Running in thread: Thread-1

Because Django signals execute synchronously, the signal handler always runs in the same thread as the function that triggered it, we can confirm that Django signals are synchronous by default.

Conclusion:
Django signals are executed synchronously by default, meaning that Django waits for the signal handler to complete before proceeding. 
Since Django signals run in the same thread as the function that triggered them, a long-running signal handler can block execution. 
To make them asynchronous, you need to run them in a separate thread or a task queue.
