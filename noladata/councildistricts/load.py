import os

from django.contrib.gis.utils import LayerMapping

from ..load import get_processed_data_file
from .models import CouncilDistrict, councildistrict_mapping


def from_shapefile(strict=False, progress=True, verbose=False, **kwargs):
    """
    Load councildistrict data into the database from the processed shapefile.
    """
    filename = os.path.join('councildistricts', 'councildistricts.shp')
    shp = get_processed_data_file(filename)
    mapping = LayerMapping(CouncilDistrict, shp, councildistrict_mapping,
                           transform=False)
    mapping.save(strict=strict, progress=progress, verbose=verbose, **kwargs)


def load(**kwargs):
    from_shapefile(**kwargs)
