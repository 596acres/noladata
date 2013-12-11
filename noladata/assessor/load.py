from pyquery import PyQuery

from .models import ParcelAssessorRecord


NOLADATA_ASSESSOR_SUMMARY_URL = 'http://qpublic9.qpublic.net/getlaParcel.php?county=la_orleans&select=' # + geopin
BASE_ASSESSOR_URL = 'http://qpublic9.qpublic.net/la_orleans_display.php'


def get_assessor_summary_value(d, key):
    key_cell = d('td *:contains("%s")' % key).parents('td')
    if not key_cell:
        key_cell = d('td:contains("%s")' % key)
    return key_cell.next()


def get_assessor_summary_value_text(d, key):
    cell = get_assessor_summary_value(d, key)
    if cell:
        return cell.text().strip()


def open_assessor_page(parcel):
    assessor_record = get_assessor_record(parcel)
    return PyQuery(url=BASE_ASSESSOR_URL + '?KEY=' + assessor_record.key)


def get_assessor_record(parcel):
    """
    Fetch this parcel's assessor record or create one by scraping.
    """
    try:
        return ParcelAssessorRecord.objects.get(parcel=parcel)
    except ParcelAssessorRecord.DoesNotExist:
        d = PyQuery(url=NOLADATA_ASSESSOR_SUMMARY_URL + str(parcel.geopin))
        assessor_record = ParcelAssessorRecord(
            address=get_assessor_summary_value_text(d, 'Location Address'),
            key=get_assessor_summary_value(d, 'Selected Parcel').find('a').text(),
            owner_name=get_assessor_summary_value_text(d, 'Name'),
            owner_address=get_assessor_summary_value_text(d, 'Mailing Address'),
            parcel=parcel,
            property_class=get_assessor_summary_value_text(d, 'Property Class'),
        )
        assessor_record.save()
        return assessor_record


def get_owner_and_parcel_information_table(d):
    """
    Find the table with its first row = "Owner and Parcel Information"
    """
    table = d('td.table_header:contains("Owner and Parcel Information")')
    while table and table.not_('table'):
        table = table.parent()
    return table


def load_tax_bill_number(parcel):
    """
    Load an address's tax bill number from the Orleans Parish Assessor's
    Office, eg:

        http://qpublic9.qpublic.net/la_orleans_display.php?KEY=1847-MONTEGUTST
    """
    d = open_assessor_page(parcel)

    table = get_owner_and_parcel_information_table(d)

    # Find the cell with the text "Tax Bill Number" in it
    tax_bill_number_header = table.find('td *:contains("Tax Bill Number")').parents('td')

    # Find the next cell, don't forget to strip
    try:
        return tax_bill_number_header.next().text().strip()
    except Exception:
        return None
