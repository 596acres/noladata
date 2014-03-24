import os

from django.contrib.gis.utils import LayerMapping

from ..load import get_processed_data_file
from .models import ZoningDistrict, zoningdistrict_mapping


def from_shapefile(strict=False, progress=True, verbose=False, **kwargs):
    """
    Load zoning data into the database from the processed shapefile.
    """
    shp = get_processed_data_file(os.path.join('zoning', 'zoning.shp'))
    mapping = LayerMapping(ZoningDistrict, shp, zoningdistrict_mapping,
                           transform=False)
    mapping.save(strict=strict, progress=progress, verbose=verbose, **kwargs)


def load(**kwargs):
    from_shapefile(**kwargs)
