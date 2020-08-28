from django.db import models


class Country(models.Model):
    name = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(unique=True, max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return self.name

    def can_delete(self):
        user_profiles_count = self.regularuserprofile_set.count()
        psy_profiles_count = self.psychologistuserprofile_set.count()
        if not psy_profiles_count and not user_profiles_count:
            return True
        return False
