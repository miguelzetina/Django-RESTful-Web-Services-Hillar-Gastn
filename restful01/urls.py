from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('drones.urls')),
    url(r'^api-auth/', include('rest_framework.urls'))
]
