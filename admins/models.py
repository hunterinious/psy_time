from django.db import models
from users.models import AdminUser


class AdminUserProfile(models.Model):
    user = models.OneToOneField(AdminUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
