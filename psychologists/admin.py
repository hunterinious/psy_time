from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import PsychologistUser, PsychologistUserProfile


class ProfileInline(admin.TabularInline):
    model = PsychologistUserProfile


class PsychologistAdmin(UserAdmin):
    inlines = [ProfileInline]


admin.site.register(PsychologistUser, PsychologistAdmin)
