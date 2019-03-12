# -*- coding: utf-8 -*-
from __future__ import absolute_import

import graphene

from .types import CategoryType, PilotType
from ..enums import GenderChoices

from drones.models import Pilot, DroneCategory


class CreatePilot(graphene.Mutation):

    class Arguments:
        name = graphene.String()
        gender = GenderChoices()
        races_count = graphene.Int()

    pilot = graphene.Field(PilotType)
    ok = graphene.Boolean()

    @staticmethod
    def mutate(self, info, name, gender, races_count):
        pilot = Pilot.objects.create(
            name=name, gender=gender, races_count=races_count
        )
        ok = True
        return CreatePilot(pilot=pilot, ok=ok)


class CreateDroneCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    ok = graphene.Boolean()
    drone_category = graphene.Field(CategoryType)

    @staticmethod
    def mutate(self, info, name):
        drone_category = DroneCategory.objects.create(name=name)
        ok = False
        return CreateDroneCategory(drone_category=drone_category)


class MyMutations(graphene.ObjectType):
    create_pilot = CreatePilot.Field()
    create_drone_category = CreateDroneCategory.Field()
