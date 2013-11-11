from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _


class Case(models.Model):
    """
    A Code Enforcement case as represented in "CE Active Pipeline":

        https://data.nola.gov/dataset/CE-Active-Pipeline/8pqz-ftzc
    """

    #
    # Address
    #
    location = models.CharField(_('location'),
        max_length=100,
        blank=True,
        null=True,
    )
    city = models.CharField(_('city'),
        max_length=100,
        blank=True,
        null=True,
    )
    state = models.CharField(_('state'),
        max_length=50,
        blank=True,
        null=True,
    )
    zipcode = models.CharField(_('zipcode'),
        max_length=15,
        blank=True,
        null=True,
    )

    #
    # Geo
    #
    geopin = models.CharField(_('geopin'),
        max_length=15,
        blank=True,
        null=True,
        help_text=_('The geopin, which should match the geopin field in the '
                    'parcel database'),
    )
    geoaddress = models.CharField(_('geoaddress'),
        max_length=100,
        blank=True,
        null=True,
        help_text=_("This seems incorrect, but we'll hold onto it"),
    )
    geom = models.PointField(_('geom'),
        help_text=_('The point given by xpos and ypos'),
    )

    #
    # Case details and status
    #
    caseid = models.CharField(_('caseid'),
        max_length=15,
    )
    caseno = models.CharField(_('caseno'),
        max_length=15,
    )
    o_c = models.CharField(_('o_c'),
        max_length=15,
        help_text=_('open / closed'),
    )
    stage = models.CharField(_('stage'),
        max_length=150,
    )
    statdate = models.DateTimeField(_('statdate'),
        blank=True,
        null=True,
    )
    keystatus = models.TextField(_('keystatus'),
        blank=True,
        null=True,
    )
    initinspection = models.DateTimeField(_('initinspection'),
        blank=True,
        null=True,
    )
    initinspresult = models.CharField(_('stage'),
        max_length=150,
        blank=True,
        null=True,
    )
    prevhearingdate = models.DateTimeField(_('prevhearingdate'),
        blank=True,
        null=True,
    )
    prevhearingresult = models.CharField(_('stage'),
        max_length=150,
        blank=True,
        null=True,
    )
    casefiled = models.DateTimeField(_('casefiled'),
        blank=True,
        null=True,
    )
    lastupload = models.DateTimeField(_('lastupload'),
        blank=True,
        null=True,
    )

    objects = models.GeoManager()
