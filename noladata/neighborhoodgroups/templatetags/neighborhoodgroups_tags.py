from django import template

from inplace.boundaries.templatetags.boundaries_tags import (BaseAllBoundariesTag)

from ..models import NeighborhoodGroup


class GetNeighborhoodGroups(BaseAllBoundariesTag):

    def get_value(self, context):
        return NeighborhoodGroup.objects.all().order_by('label')


register = template.Library()
register.tag(GetNeighborhoodGroups)
