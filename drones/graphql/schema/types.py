# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from graphene_django.types import DjangoObjectType

from drones.models import DroneCategory, Drone, Pilot, Competition


class CategoryType(DjangoObjectType):
    class Meta:
        model = DroneCategory


class DroneType(DjangoObjectType):
    class Meta:
        model = Drone


class PilotType(DjangoObjectType):
    class Meta:
        model = Pilot


class CompetitionType(DjangoObjectType):
    class Meta:
        model = Competition


class OwnerType(DjangoObjectType):
    class Meta:
        model = User
