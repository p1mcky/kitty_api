from django_filters import rest_framework as filters

from cats.models import Breed, Kitty


class KittyFilter(filters.FilterSet):
    breed = filters.ModelMultipleChoiceFilter(
        field_name='breed__slug',
        queryset=Breed.objects.all(),
        to_field_name='slug'
    )

    class Meta:
        model = Kitty
        fields = ['breed']
