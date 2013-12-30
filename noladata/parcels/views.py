import json
import geojson

from django.contrib.gis.geos import Polygon
from django.views.generic import DetailView, TemplateView, View

from inplace.views import GeoJSONListView, GeoJSONResponseMixin
from .models import Parcel


class OverlapGeoJSONView(GeoJSONResponseMixin, View):

    def get_feature(self, parcel):
        pbo = parcel.parcelbuildingoverlap_set.all()[0]
        return geojson.Feature(
            parcel.pk,
            geometry=json.loads(parcel.centroid.geojson),
            properties={
                'id': parcel.pk,
                'percent_overlap': round(pbo.percent_parcel_covered, 2),
            }
        )

    def get_features(self):
        print self.request.GET
        percent_gt = self.request.GET.get('percent_gt', 0)
        percent_lte = self.request.GET.get('percent_lte', 0)
        parcels = Parcel.objects.filter(
            parcelbuildingoverlap__percent_parcel_covered__gt=percent_gt,
            parcelbuildingoverlap__percent_parcel_covered__lte=percent_lte,
        ).select_related('parcelbuildingoverlap').centroid()

        area_gt = float(self.request.GET.get('area_gt', 0))
        area_lte = float(self.request.GET.get('area_lte', 0))
        parcels = filter(lambda p: area_gt < p.calculate_area() <= area_lte, list(parcels))

        print 'count', len(parcels)
        return [self.get_feature(parcel) for parcel in parcels]

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})


class OverlapMapView(TemplateView):
    template_name = 'noladata/parcels/overlap.html'


class OverlapDetailGeoJSONView(GeoJSONResponseMixin, DetailView):
    model = Parcel

    def get_feature(self, obj):
        return geojson.Feature(
            obj.pk,
            geometry=json.loads(obj.geom.geojson),
            properties={
                'id': obj.pk,
                'type': obj._meta.model_name,
            }
        )

    def get_features(self):
        pk = self.kwargs.get('pk', None)
        parcel = Parcel.objects.get(pk=pk)
        objs = []
        objs.append(parcel)
        pbo = parcel.parcelbuildingoverlap_set.all()[0]
        for building in pbo.buildings.all():
            objs.append(building)
        return [self.get_feature(obj) for obj in objs]

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})


class OverlapDetailView(DetailView):
    model = Parcel
    template_name = 'noladata/parcels/overlap_detail.html'


class GeoJSONPolygonView(GeoJSONListView):
    model = Parcel

    def get_feature(self, parcel):
        return geojson.Feature(
            parcel.pk,
            geometry=json.loads(parcel.geojson),
            properties=self.get_properties(parcel),
        )

    def get_properties(self, parcel):
        return {
            'address': parcel.address,
        }

    def get_queryset(self):
        try:
            bbox = Polygon.from_bbox(self.request.GET['bbox'].split(','))
            return super(GeoJSONPolygonView, self).get_queryset().filter(
                geom__intersects=bbox,
            ).geojson(precision=6)
        except KeyError:
            return Parcel.objects.none()
