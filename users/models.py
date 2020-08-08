from enum import Enum
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class UserTypes(Enum):
    regular_user = "regular_user"
    psychologist_user = "psychologist_user"
    admin_user = "admin_user"


class CustomUserManager(BaseUserManager):
    def create_user(self, email,  username, password):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=60, unique=True)
    user_type = models.CharField(max_length=50, choices=[(tag.name, tag.value) for tag in UserTypes])
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_staff

    # Does this user have permission to view this app?
    def has_module_perms(self, app_label):
        return True


class RegularUser(CustomUser):
    class Meta:
        proxy = True


class PsychologistUser(CustomUser):
    class Meta:
        proxy = True


class AdminUser(CustomUser):
    class Meta:
        proxy = True


class RegularUserProfile(models.Model):
    avatar = models.ImageField(upload_to="avatars", default="avatars/avatar.jpg")
    location_city = models.CharField(null=True, blank=True, max_length=50)
    location_country = models.CharField(null=True, blank=True, max_length=50)
    user = models.OneToOneField(RegularUser, on_delete=models.CASCADE)
