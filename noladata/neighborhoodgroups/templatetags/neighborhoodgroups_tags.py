from django import template

from classytags.arguments import Argument
from classytags.core import Options
from classytags.helpers import AsTag

from ..models import NeighborhoodGroup


class GetNeighborhoodGroups(AsTag):
    options = Options(
        'as',
        Argument('varname', required=True, resolve=False),
    )

    def get_value(self, context):
        return NeighborhoodGroup.objects.all().order_by('label')


register = template.Library()
register.tag(GetNeighborhoodGroups)
