import graphene

from drones.graphql.schema import Query as drone_query


class Query(drone_query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query)
