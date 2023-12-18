from django.urls import path
from .views import get_status

app_name = 'tasks'

urlpatterns = [
    path('', get_status, name='get_status'),
]