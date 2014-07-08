import csv
import os
import traceback

from django.contrib.gis.geos import Point

from ..load import get_processed_data_file
from .models import UncommittedProperty


def save_row(row):
    """
    Save a row.

    If the row already exists, make it current. Otherwise create it as new.
    """
    kwargs = {
        'city': row['City'],
        'state': row['State'],
        'zip': row['Zip'],
        'geom': Point(float(row['X']), float(row['Y'])),
    }
    instance, created = UncommittedProperty.objects.get_or_create(
        identifier=row['Identifier'],
        property_address=row['Property Address'],
        defaults=kwargs
    )
    instance.status = 'current'
    instance.save()
    return instance


def from_csv():
    """
    Load uncommitted property data into the database from the processed csv.
    """
    csvpath = os.path.join('nora', 'uncommitted_properties',
                           'uncommitted_properties.csv')
    csvfile = open(get_processed_data_file(csvpath), 'r')

    # Mark all existing UncommittedProperty instances as old
    UncommittedProperty.objects.all().update(status='old')
    for row in csv.DictReader(csvfile):
        try:
            save_row(row)
        except Exception:
            traceback.print_exc()
            print 'Could not save row: ' + str(row)
            raise


def load():
    from_csv()
