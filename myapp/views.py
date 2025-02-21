from django.shortcuts import render,HttpResponse
import threading
from .models import MainModel
# Create your views here.

def test_signal_thread(request):
    print(f"[Caller] Running in thread: {threading.current_thread().name}")
    MainModel.objects.create(name="Test User")  
    return HttpResponse("Check the console for thread names.")


# by default, Django signals run in the same thread as the caller.
# Since Django signals are synchronous by default, they execute immediately in the same thread as the function that triggered them.
# This means that if a signal handler takes time to execute, it blocks the main execution thread until it completes.
