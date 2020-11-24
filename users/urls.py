from django.urls import path
from .views import RegularUserAndProfileView


urlpatterns = [
    path('profile/<int:pk>/retrieve-update', RegularUserAndProfileView.as_view(), name='api-regular-profile')
]
