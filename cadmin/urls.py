from django.urls import path
from .views import PsychologistProfileCreateView


urlpatterns = [
    path("users/profiles/create_psy_profile", PsychologistProfileCreateView.as_view(), name='psy-profile-create')
]