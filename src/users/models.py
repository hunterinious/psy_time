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
    username = models.CharField(unique=True, max_length=30)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    user_type = models.CharField(max_length=50, choices=[(tag.name, tag.value) for tag in UserTypes])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
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


class PsychologistUserProfile(models.Model):
    birth_date = models.DateField(null=False)
    about = models.TextField(null=False)
    work_experience = models.TextField(null=False)
    price = models.IntegerField(null=False)
    time = models.IntegerField(null=False)
    user = models.OneToOneField(PsychologistUser, on_delete=models.CASCADE)


class AdminUserProfile(models.Model):
    user = models.OneToOneField(AdminUser, on_delete=models.CASCADE)


class PsychologistStatus(models.Model):
    name = models.CharField(unique=True, max_length=50)
    psychologist = models.ManyToManyField(PsychologistUserProfile, related_name="statuses")


class PsychologistWorkFormat(models.Model):
    name = models.CharField(unique=True, max_length=50)
    psychologist = models.ManyToManyField(PsychologistUserProfile, related_name="formats")


class PsychologistTheme(models.Model):
    name = models.CharField(unique=True, max_length=50)
    psychologist = models.ManyToManyField(PsychologistUserProfile, related_name="themes")


class PsychologistApproach(models.Model):
    name = models.CharField(unique=True, max_length=50)
    psychologist = models.ManyToManyField(PsychologistUserProfile, related_name="approaches")


class PsychologistSpecialization(models.Model):
    name = models.CharField(unique=True, max_length=50)
    psychologist = models.ManyToManyField(PsychologistUserProfile, related_name="specializations")


class PsychologistEducation(models.Model):
    name = models.CharField(unique=True, max_length=50)
    psychologist = models.ManyToManyField(PsychologistUserProfile, related_name="educations")


class PsychologistSecondaryEducation(models.Model):
    name = models.CharField(unique=True, max_length=50)
    psychologist = models.ManyToManyField(PsychologistUserProfile, related_name="secondary_educations")


class PsychologistLanguages(models.Model):
    name = models.CharField(unique=True,  max_length=50)
    psychologist = models.ManyToManyField(PsychologistUserProfile, related_name="languages")


class Image(models.Model):
    name = models.CharField(unique=True, max_length=255)
    image = models.ImageField(null=False)
    psychologist = models.ForeignKey(PsychologistUserProfile, on_delete=models.CASCADE)
