from rest_framework import viewsets

from .serializers import HeroSerializer, VillainSerializer
from .models import Hero, VillainModel


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer


class VillainViewSet(viewsets.ModelViewSet):
    queryset = VillainModel.objects.all().order_by('name')
    serializer_class = VillainSerializer
