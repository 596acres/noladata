import os

from django.contrib.gis.utils import LayerMapping

from ..load import get_processed_data_file
from .models import ZipCode, zipcode_mapping


def from_shapefile(strict=False, progress=True, verbose=False, **kwargs):
    """
    Load zipcode data into the database from the processed shapefile.
    """
    zipcode_shp = get_processed_data_file(os.path.join('zipcodes',
                                                       'zipcodes.shp'))
    mapping = LayerMapping(ZipCode, zipcode_shp, zipcode_mapping,
                           transform=False)
    mapping.save(strict=strict, progress=progress, verbose=verbose, **kwargs)


def load(**kwargs):
    from_shapefile(**kwargs)
