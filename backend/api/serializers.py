import webcolors
from rest_framework import serializers

from cats.models import Breed, Kitty, Rating


class Hex2NameColor(serializers.Field):
    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        try:
            data = webcolors.hex_to_name(data)
        except ValueError:
            raise serializers.ValidationError('Для этого цвета нет имени')
        return data


class BreedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Breed
        fields = '__all__'


class KittyListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kitty
        fields = ('id', 'name', 'age')


class RatingSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Rating
        fields = ['username', 'rating']

    def create(self, validated_data):
        validated_data['kitty_id'] = self.context['kitty_id']
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class KittySerializer(serializers.ModelSerializer):
    color = Hex2NameColor()
    breed = serializers.PrimaryKeyRelatedField(
        queryset=Breed.objects.all(), required=True
    )
    owner = serializers.StringRelatedField(source='owner.username')
    ratings = RatingSerializer(source='rating_set', many=True, read_only=True)

    class Meta:
        model = Kitty
        fields = (
            'id',
            'name',
            'color',
            'age',
            'breed',
            'description',
            'owner',
            'ratings'
        )
        read_only_fields = ('owner', )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['breed'] = getattr(instance.breed, 'name', None)
        return data

    def create(self, validated_data):
        owner = self.context.get('request').user
        validated_data['owner'] = owner
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.color = validated_data.get('color', instance.color)
        instance.age = validated_data.get('age', instance.age)
        instance.description = validated_data.get(
            'description', instance.description
        )
        instance.breed = validated_data.get('breed', instance.breed)
        instance.save()
        return instance
