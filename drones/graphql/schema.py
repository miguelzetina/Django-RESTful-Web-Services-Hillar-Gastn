# -+- coding: utf-8 -*-
import graphene

from graphene_django.types import DjangoObjectType

from drones.models import DroneCategory, Drone, Pilot, Competition


class CategoryType(DjangoObjectType):
    class Meta:
        model = DroneCategory


class DroneType(DjangoObjectType):
    class Meta:
        model = Drone


class Query(object):
    all_categories = graphene.List(CategoryType)
    all_drones = graphene.List(DroneType)

    def resolve_all_categories(self, info, **kwargs):
        return DroneCategory.objects.all()

    def resolve_all_drones(self, info, **kwargs):
        return Drone.objects.select_related('drone_category').all()
