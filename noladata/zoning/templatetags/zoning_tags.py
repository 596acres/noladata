from django import template

from inplace.boundaries.templatetags.boundaries_tags import (
    BaseAllBoundariesTag,
    BaseGetBoundaryTag)

from ..models import ZoningDistrict


class GetZoningDistrict(BaseGetBoundaryTag):

    def get_boundary_model(self):
        return ZoningDistrict


class GetZoningDistricts(BaseAllBoundariesTag):

    def get_value(self, context):
        return ZoningDistrict.objects.all().order_by('label')


register = template.Library()
register.tag(GetZoningDistrict)
register.tag(GetZoningDistricts)
