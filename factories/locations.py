from locations.models import Country, City
import factory


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country
        django_get_or_create = ('name', )

    name = factory.Faker('country')


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = City
        django_get_or_create = ('name',)

    name = factory.Faker('city')
    country = factory.SubFactory(CountryFactory)


class CountryWithCitiesFactory(CountryFactory):
    @factory.post_generation
    def cities(self, create, extracted):
        if not create:
            return
        if extracted:
            for n in range(extracted):
                CityFactory(country=self)
