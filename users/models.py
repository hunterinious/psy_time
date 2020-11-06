from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from locations.models import City


class CustomUserManager(BaseUserManager):
    def create_user(self, email,  username, password, user_type):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            user_type=user_type
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
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

    class UserTypes(models.TextChoices):
        REGULAR_USER = 'R', _('Regular')
        PSYCHOLOGIST_USER = 'P', _('Psychologist')
        ADMIN_USER = 'A', _('Admin')

    email = models.EmailField(max_length=60, unique=True)
    user_type = models.CharField(max_length=50, choices=UserTypes.choices)
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


class PsychologistUserManager(models.Manager):
    def get_user(self, id):
        return self.model.objects.get(id=id)

    def get_reviews(self, id):
        return self.model.objects.get(id=id).psy_reviews.all()

    def get_reviews_count(self, id):
        return self.model.objects.get(id=id).psy_reviews.count()


class PsychologistUser(CustomUser):
    class Meta:
        proxy = True

    objects = PsychologistUserManager()


class AdminUser(CustomUser):
    class Meta:
        proxy = True


class RegularUserProfile(models.Model):
    avatar = models.ImageField(upload_to="avatars", default="avatars/avatar.jpg")
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.SET_NULL)
    user = models.OneToOneField(RegularUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
