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


def load_building_overlaps(count=1000):
    """
    For every parcel, find out how much of it is overlapped by a building (or
    buildings) and which.
    """
    parcels = Parcel.objects.filter(parcelbuildingoverlap=None)[:count]
    for parcel in parcels:
        try:
            parcel.calculate_building_overlap()
        except Exception:
            print '*** FAILED with parcel %s' % parcel.objectid
            import traceback
            traceback.print_exc()
            continue
    print 'Loaded building overlaps for %d parcels, %d more to go' % (
        parcels.count(),
        Parcel.objects.filter(parcelbuildingoverlap=None).count()
    )
    return parcels.count()


def load(**kwargs):
    from_shapefile(**kwargs)
