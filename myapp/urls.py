from django.urls import path
from .views import test_signal_thread

urlpatterns = [
    path('', test_signal_thread, name='test_signal_thread'),
]
