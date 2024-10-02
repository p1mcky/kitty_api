from django.contrib.auth import get_user_model
from django.core.validators import (
    MaxValueValidator, MinValueValidator, RegexValidator
)
from django.db import models


User = get_user_model()


class Breed(models.Model):
    name = models.CharField(
        max_length=75, unique=True, verbose_name='Название'
    )
    slug = models.SlugField(max_length=75, unique=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'

    def __str__(self):
        return self.name


class Kitty(models.Model):
    name = models.CharField(
        'Имя', max_length=50, validators=[RegexValidator(r'^[a-zA-Zа-яА-Я]+$')]
    )
    color = models.CharField('Возраст', max_length=16)
    age = models.PositiveSmallIntegerField(
        'Возраст', validators=[MinValueValidator(0)]
    )
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    description = models.TextField('Описание', max_length=500)
    owner = models.ForeignKey(
        User, related_name='cats',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Котёнок'
        verbose_name_plural = 'Котята'
        unique_together = ('name', 'breed', 'color', 'age')

    def __str__(self):
        return self.name


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kitty = models.ForeignKey(Kitty, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    class Meta:
        unique_together = ('user', 'kitty')
