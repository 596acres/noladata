from django import template

from inplace.boundaries.templatetags.boundaries_tags import (
    BaseAllBoundariesTag,
    BaseGetBoundaryTag)

from ..models import NeighborhoodGroup


class GetNeighborhoodGroup(BaseGetBoundaryTag):

    def get_boundary_model(self):
        return NeighborhoodGroup


class GetNeighborhoodGroups(BaseAllBoundariesTag):

    def get_value(self, context):
        return NeighborhoodGroup.objects.all().order_by('label')


register = template.Library()
register.tag(GetNeighborhoodGroup)
register.tag(GetNeighborhoodGroups)
