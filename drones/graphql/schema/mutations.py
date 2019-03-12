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

    @staticmethod
    def mutate(self, info, name, gender, races_count):
        pilot = Pilot.objects.create(
            name=name, gender=gender, races_count=races_count
        )
        return CreatePilot(pilot=pilot)


class CreateDroneCategory(graphene.Mutation):

    class Arguments:
        name = graphene.String()

    drone_category = graphene.Field(CategoryType)

    @staticmethod
    def mutate(self, info, name):
        drone_category = DroneCategory.objects.create(name=name)
        return CreateDroneCategory(drone_category=drone_category)


class MyMutations(graphene.ObjectType):
    create_pilot = CreatePilot.Field()
    create_drone_category = CreateDroneCategory.Field()
