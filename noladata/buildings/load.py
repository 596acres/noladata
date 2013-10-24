import os

from django.contrib.gis.utils import LayerMapping

from ..load import get_processed_data_file
from .models import Building, building_mapping


def from_shapefile(strict=False, progress=True, verbose=False, **kwargs):
    """
    Load building data into the database from the processed shapefile.
    """
    building_shp = get_processed_data_file(os.path.join('buildings',
                                                        'buildings.shp'))
    mapping = LayerMapping(Building, building_shp, building_mapping,
                           transform=False)
    mapping.save(strict=strict, progress=progress, verbose=verbose, **kwargs)


def load(**kwargs):
    from_shapefile(**kwargs)
