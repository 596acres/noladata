import os
import re

from fastkml import kml
import lxml

from django.contrib.gis import geos

from ..load import get_processed_data_file
from .models import NeighborhoodGroup


def _clean_description(description):
    """Try to wipe HTML from the given description."""
    description = description.replace('&nbsp;', ' ')
    description = lxml.html.fromstring(description).text_content()
    (description, n) = re.subn('\s+', ' ', description)
    return description


def _get_full_name(description):
    """
    Attempt to parse the full name of the neighborhood group from its
    description.
    """
    description = re.sub('Extent of( the)? ', '', description)
    description = re.sub('\.? ?(Contact|Email|See|Visit).*', '', description)
    description = description.strip()
    description = re.sub('\.$', '', description)
    return description


def _get_url(description):
    """Try to get a linked-to URL from the given description."""
    match = re.match('.*href="([^"]+)".*', description)
    if match:
        return match.group(1)
    return None


def _get_features(filename):
    k = kml.KML()
    k.from_string(open(filename, 'r').read())
    return list(k.features())[0].features()


def _get_filename():
    return get_processed_data_file(os.path.join('neighborhoodgroups',
                                                'NOLANeighborhoodGroups.kml'))


def _get_geometry(group):
    try:
        wkt, n = re.subn(' 0.0', '', group.geometry.wkt)
        return geos.MultiPolygon(geos.fromstr(wkt))
    except Exception:
        return None


def from_kml(strict=False, progress=True, verbose=False, **kwargs):
    """
    Load neighborhood group data into the database from the KML shapefile.
    """
    for group in _get_features(_get_filename()):
        # Skip if we have a group with this name already
        if NeighborhoodGroup.objects.filter(name=group.name).exists():
            continue

        # Try to get geometry and move on if we can't
        geometry = _get_geometry(group)
        if not geometry:
            print 'Did not get geometry from %s' % group.name
            continue
        else:
            print geometry

        description = _clean_description(group.description)
        saved_group = NeighborhoodGroup(
            description=description,
            full_name=_get_full_name(description),
            geometry=geometry,
            label=group.name,
            name=group.name,
            url=_get_url(group.description),
        )
        saved_group.save()


def load(**kwargs):
    from_kml(**kwargs)
