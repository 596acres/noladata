from django.db import models


class ParcelAssessorRecord(models.Model):
    """
    Some useful information the assessor stores about parcels
    """
    address = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        help_text='The address the assessor uses for this parcel',
    )
    key = models.CharField(
        max_length=100,
        help_text="The key the assessor uses for this parcel's card",
    )
    owner_name = models.CharField(
        max_length=300,
        blank=True,
        null=True,
    )
    owner_address = models.CharField(
        max_length=300,
        blank=True,
        null=True,
    )
    property_class = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    last_checked = models.DateTimeField(auto_now=True)
    parcel = models.ForeignKey('parcels.Parcel')
