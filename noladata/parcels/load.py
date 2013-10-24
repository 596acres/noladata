import os

from django.contrib.gis.utils import LayerMapping

from ..load import get_processed_data_file
from .models import Parcel, parcel_mapping


def from_shapefile(strict=False, progress=True, verbose=False, **kwargs):
    """
    Load parcel data into the database from the processed shapefile.
    """
    parcel_shp = get_processed_data_file(os.path.join('parcels', 'parcels.shp'))
    mapping = LayerMapping(Parcel, parcel_shp, parcel_mapping, transform=False)
    mapping.save(strict=strict, progress=progress, verbose=verbose, **kwargs)
