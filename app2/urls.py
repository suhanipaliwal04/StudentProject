from django.urls import path
from .views import page2  # Ensure `page2` exists in views.py

urlpatterns = [
    path('page2/', page2, name='page2'),
]
