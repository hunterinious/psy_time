from django.urls import path
from .views import (
    HelpCreateView
)


urlpatterns = [
    path('help', HelpCreateView.as_view(), name="api-help-create")
]
