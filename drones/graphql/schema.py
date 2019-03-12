# -+- coding: utf-8 -*-
import graphene

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


class Query(object):
    all_categories = graphene.List(CategoryType)
    all_drones = graphene.List(DroneType)
    all_pilots = graphene.List(PilotType)
    all_competitions = graphene.List(CompetitionType)

    category = graphene.Field(
        CategoryType, id=graphene.Int(), name=graphene.String()
    )

    drone = graphene.Field(
        DroneType, id=graphene.Int(), name=graphene.String(),
        manufacturing_date=graphene.types.datetime.DateTime(),
        inserted_timestamp=graphene.types.datetime.DateTime()
    )

    def resolve_all_categories(self, info, **kwargs):
        return DroneCategory.objects.all()

    def resolve_all_drones(self, info, **kwargs):
        return Drone.objects.select_related('drone_category').all()

    def resolve_all_pilots(self, info, **kwargs):
        return Pilot.objects.all()

    def resolve_all_competitions(self, info, **kwargs):
        return Competition.objects.all()

    def resolve_category(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return DroneCategory.objects.get(pk=id)

        if name is not None:
            return DroneCategory.objects.get(name=name)

        return None

    def resolve_drone(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Drone.objects.get(pk=id)

        if name is not None:
            return Drone.objects.get(name=name)

        return None
