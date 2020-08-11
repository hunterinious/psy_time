from django.urls import path
from .views import PsychologistStatusCreateView


urlpatterns = [
    path("psychologists/status/create", PsychologistStatusCreateView.as_view(), name='psy-status-create')
]