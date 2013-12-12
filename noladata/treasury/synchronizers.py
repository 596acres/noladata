from datetime import datetime
import os
from random import random
from time import sleep

from django.conf import settings
from django.utils.timezone import now

from external_data_sync import register, synchronizers

from ..assessor.load import load_tax_bill_number
from ..parcels.models import Parcel
from .load import load_code_lien_information
from .models import Lien, ParcelLienRecord


def parse_delinquency_date(date):
    return datetime.strptime(date, '%m/%d/%y')


def lien_kwargs(parcel, lien):
    return {
        'city_fee': lien['City Fee'],
        'code': lien['Code'],
        'collection_fee': lien['Collection Fee'],
        'delinquency_date': parse_delinquency_date(lien['Delinquency Date']),
        'interest': lien['Interest'],
        'period': lien['Period'],
        'tax_or_lien': lien['Tax or Lien'],
        'total': lien['Total'],
        'type': lien['Type'],
        'parcel': parcel,
    }


def create_or_update_lien(parcel, lien):
    kwargs = lien_kwargs(parcel, lien)
    existing_lien = Lien.objects.filter(
        parcel=parcel,
        period=kwargs['period'],
        type=kwargs['type']
    )
    if existing_lien.count() == 1:
        existing_lien.update(**kwargs)
        saved_lien = existing_lien[0]
    else:
        saved_lien = Lien(**kwargs)
        saved_lien.save()
    return saved_lien


def update_parcel_lien_record(parcel):
    """
    Create or update ParcelLienRecord for this parcel.

    Record the fact that we've seen this parcel's liens (or lack thereof).
    """
    parcel_lien_record, created = ParcelLienRecord.objects.get_or_create(
        parcel=parcel,
        defaults={ 'last_checked': now() }
    )
    if not created:
        parcel_lien_record.last_checked = now()
        parcel_lien_record.save()


class LienSynchronizer(synchronizers.Synchronizer):

    def get_geopins_from_file(self, max=1000):
        # Get geopins from our file
        geopins = None
        with open(settings.NOLADATA_TREASURY_PARCELS_GEOPINS, 'r') as geopin_file:
            geopins = [g.strip() for g in geopin_file.readlines()]

        # Save the original geopins file if it's not saved yet
        backup_filename = settings.NOLADATA_TREASURY_PARCELS_GEOPINS + '.orig'
        if not os.path.exists(backup_filename):
            with open(backup_filename, 'w') as backup_file:
                backup_file.writelines([g + '\n' for g in geopins])

        # Save only the geopins we would want to get to next
        with open(settings.NOLADATA_TREASURY_PARCELS_GEOPINS, 'w') as new_geopin_file:
            new_geopin_file.writelines([g + '\n' for g in geopins[max:]])

        return geopins[:max]

    def pick_parcels(self, data_source):
        """
        Get parcels with no ParcelLienRecord or those which were checked least
        recently.
        """
        parcels = Parcel.objects.filter(parcellienrecord=None).order_by('?')
        try:
            geopins = self.get_geopins_from_file(max=data_source.batch_size)
            preferred_parcels = parcels.filter(geopin__in=geopins)
            if preferred_parcels.count():
                parcels = preferred_parcels
        except Exception:
            pass
        count = parcels.count()
        if not count:
            parcels = Parcel.objects.order_by('parcellienrecord__last_checked')
        if count > data_source.batch_size:
            return parcels[:data_source.batch_size]
        return parcels

    def wait(self):
        """Wait a bit between parcels / external requests"""
        sleep(2 * random())

    def sync(self, data_source):
        for parcel in self.pick_parcels(data_source):
            print parcel
            try:
                tax_bill_number = load_tax_bill_number(parcel)
            except Exception:
                print ('Could not find tax_bill_number for parcel with pk %d'
                       % parcel.pk)

            if tax_bill_number:
                # TODO try to be more defensive about exceptions here
                code_lien_information = load_code_lien_information(tax_bill_number)
                print '\t', tax_bill_number
                for code_lien in code_lien_information:
                    print '\t', code_lien
                    create_or_update_lien(parcel, code_lien)

            update_parcel_lien_record(parcel)
            self.wait()


register(LienSynchronizer)
