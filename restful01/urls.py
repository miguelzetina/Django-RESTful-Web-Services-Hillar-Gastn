from django.conf.urls import url, include

from graphene_django.views import GraphQLView


urlpatterns = [
    url(r'^', include('drones.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
]
