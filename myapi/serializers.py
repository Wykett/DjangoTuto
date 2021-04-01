from rest_framework import serializers

from myapi.models import Hero, VillainModel


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'


class VillainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VillainModel
        fields = '__all__'
