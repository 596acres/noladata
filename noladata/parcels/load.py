import os

from django.contrib.gis.utils import LayerMapping

from ..buildings.models import Building
from ..load import get_processed_data_file
from .models import (BuildingOverlap, Parcel, ParcelBuildingOverlap,
                     parcel_mapping)


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
    srid = 3452
    parcels = Parcel.objects.filter(parcelbuildingoverlap=None)[:count]
    for parcel in parcels:
        buildings = Building.objects.filter_by_parcel(parcel)
        try:
            total_intersect = 0
            parcel_geometry = parcel.geom
            parcel_geometry.transform(srid)
            parcel_building_overlap = ParcelBuildingOverlap(parcel=parcel)
            parcel_building_overlap.save()
            for building in buildings:
                building_geometry = building.geom
                building_geometry.transform(srid)
                intersection = parcel_geometry.intersection(building_geometry)
                total_intersect += intersection.area
                building_overlap = BuildingOverlap(
                    building=building,
                    parcel_building_overlap=parcel_building_overlap,
                    percent_building_within_parcel=(intersection.area / building_geometry.area) * 100,
                )
                building_overlap.save()
            percent_parcel_covered = (total_intersect / parcel_geometry.area) * 100
            #print 'percent_parcel_covered', percent_parcel_covered
            parcel_building_overlap.percent_parcel_covered = percent_parcel_covered
            parcel_building_overlap.save()
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
