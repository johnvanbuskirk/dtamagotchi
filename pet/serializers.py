from django.contrib.auth.models import User, Group
from pet.models import Pet
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group


class PetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pet
