from django.conf.urls import patterns, url

from .views import (OverlapDetailView, OverlapDetailGeoJSONView,
                    OverlapGeoJSONView, OverlapMapView, GeoJSONPolygonView)


urlpatterns = patterns('',

    url(r'^overlap/details/(?P<pk>\d+)/geojson/$',
        OverlapDetailGeoJSONView.as_view(),
        name='parcel_overlap_details_geojson'),

    url(r'^overlap/details/(?P<pk>\d+)/$', OverlapDetailView.as_view(),
        name='parcel_overlap_details'),

    url(r'^overlap/map/$', OverlapMapView.as_view(),
        name='parcel_overlap_map'),

    url(r'^overlap/', OverlapGeoJSONView.as_view(), name='parcel_overlap'),

    url(r'^geojson/', GeoJSONPolygonView.as_view(), name='parcel_geojson'),

)
