import os

from django.contrib.gis.utils import LayerMapping

from ..load import get_processed_data_file
from .models import Address, address_mapping


def from_shapefile(strict=False, progress=True, verbose=False, **kwargs):
    """
    Load address data into the database from the processed shapefile.
    """
    address_shp = get_processed_data_file(os.path.join('addresses',
                                                       'addresses.shp'))
    mapping = LayerMapping(Address, address_shp, address_mapping,
                           transform=False)
    mapping.save(strict=strict, progress=progress, verbose=verbose, **kwargs)
