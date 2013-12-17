from django import template

from classytags.arguments import Argument
from classytags.core import Options
from classytags.helpers import AsTag

from ..models import ZipCode


class GetZipCodes(AsTag):
    options = Options(
        'as',
        Argument('varname', required=True, resolve=False),
    )

    def get_value(self, context):
        return ZipCode.objects.all().order_by('label')


register = template.Library()
register.tag(GetZipCodes)
