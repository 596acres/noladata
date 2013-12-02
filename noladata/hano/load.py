import csv
import os

from ..load import get_processed_data_file
from .models import ScatteredSite


def scattered_sites():
    filename = os.path.join('hano', 'scattered_sites_for_disposition',
                            'HANO_Scattered_Sites_for_Disposition.csv')
    sites_file = csv.DictReader(open(get_processed_data_file(filename)))
    for site in sites_file:
        saved_site = ScatteredSite(
            address=site['Property Address'],
            units=int(site['Units']),
        )
        saved_site.save()


def load():
    scattered_sites()
