from django.db import models


class ParcelLienRecord(models.Model):
    last_checked = models.DateTimeField()
    tax_bill_number = models.CharField(max_length=25, null=True, blank=True)
    parcel = models.ForeignKey('parcels.Parcel')


class Lien(models.Model):
    """
    A Lien as recorded by the City of New Orleans Bureau of the Treasury.

    """
    city_fee = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    collection_fee = models.CharField(max_length=50)
    delinquency_date = models.DateField()
    interest = models.CharField(max_length=50)
    period = models.CharField(max_length=25, blank=True, null=True)
    tax_or_lien = models.CharField(max_length=50)
    total = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    added = models.DateTimeField(auto_now_add=True)
    parcel = models.ForeignKey('parcels.Parcel')
