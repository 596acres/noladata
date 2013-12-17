from django.conf.urls import patterns, url

from .views import ZipCodeDetailView


urlpatterns = patterns('',

    url(r'^(?P<label>\d+)/geojson/$', ZipCodeDetailView.as_view(),
        name='zipcode_details_geojson'),

)
