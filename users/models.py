from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from locations.models import City, Timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, user_type):
        user = self.model(
            email=self.normalize_email(email),
            user_type=user_type
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            user_type=CustomUser.UserTypes.ADMIN_USER
        )

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def get_users(self):
        return self.all()

    def get_psychologists_users(self):
        return self.filter(user_type=self.model.UserTypes.PSYCHOLOGIST_USER)


class CustomUser(AbstractUser, PermissionsMixin):
    username = None
    first_name = None
    last_name = None

    class UserTypes(models.TextChoices):
        REGULAR_USER = 'R', _('Regular')
        PSYCHOLOGIST_USER = 'P', _('Psychologist')
        ADMIN_USER = 'A', _('Admin')

    email = models.EmailField(max_length=60, unique=True)
    user_type = models.CharField(max_length=50, choices=UserTypes.choices)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ()

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_staff

    # Does this user have permission to view this app?
    def has_module_perms(self, app_label):
        return True

    @property
    def profile(self):
        user_type = self.user_type
        if user_type == CustomUser.UserTypes.REGULAR_USER:
            return self.regularuserprofile
        elif user_type == CustomUser.UserTypes.PSYCHOLOGIST_USER:
            return self.psychologistuserprofile
        elif user_type == CustomUser.UserTypes.ADMIN_USER:
            return None


class RegularUser(CustomUser):
    class Meta:
        proxy = True


class PsychologistUser(CustomUser):
    class Meta:
        proxy = True


class AdminUser(CustomUser):
    class Meta:
        proxy = True


class RegularUserProfileManager(models.Manager):
    def create_profile(self, user, name, **kwargs):
        self.create(user=user, name=name, **kwargs)


class RegularUserProfile(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, validators=[MinLengthValidator(3)])
    avatar = models.ImageField(upload_to="avatars", default="avatars/avatar.jpg")
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.SET_NULL)
    timezone = models.ForeignKey(Timezone,  on_delete=models.PROTECT)
    user = models.OneToOneField(RegularUser, on_delete=models.CASCADE)

    objects = RegularUserProfileManager()

    def __str__(self):
        return str(self.user)
