from django.contrib import admin
from .models import PsychologistUser, PsychologistUserProfile


class ProfileInline(admin.TabularInline):
    model = PsychologistUserProfile


class PsychologistAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]


admin.site.register(PsychologistUser, PsychologistAdmin)
