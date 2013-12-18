from django.conf.urls import patterns, url

from .views import NeighborhoodGroupDetailView


urlpatterns = patterns('',

    url(r'^(?P<label>[^/]+)/geojson/$', NeighborhoodGroupDetailView.as_view(),
        name='neighborhoodgroup_details_geojson'),

)
