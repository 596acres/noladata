from pyquery import PyQuery


BASE_ASSESSOR_URL = 'http://qpublic9.qpublic.net/la_orleans_display.php'


def open_assessor_page(address):
    return PyQuery(url=BASE_ASSESSOR_URL + '?KEY=' + address)


def combine_address(street_number, street_name, street_type=None,
                    street_direction=None):
    """
    Put an address in a format the assessor's site will understand
    """
    street = ''.join([s.upper() for s
                      in (street_direction, street_name, street_type) if s])
    return '%s-%s' % (street_number, street)


def get_owner_and_parcel_information_table(d):
    """
    Find the table with its first row = "Owner and Parcel Information"
    """
    table = d('td.table_header:contains("Owner and Parcel Information")')
    while table and table.not_('table'):
        table = table.parent()
    return table


def load_tax_bill_number(street_number, street_name, street_type,
                         street_direction=None):
    """
    Load an address's tax bill number from the Orleans Parish Assessor's
    Office, eg:

        http://qpublic9.qpublic.net/la_orleans_display.php?KEY=1847-MONTEGUTST
    """
    d = open_assessor_page(combine_address(street_number, street_name,
                                           street_type,
                                           street_direction=street_direction))

    table = get_owner_and_parcel_information_table(d)

    # Find the cell with the text "Tax Bill Number" in it
    tax_bill_number_header = table.find('td *:contains("Tax Bill Number")').parents('td')

    # Find the next cell, don't forget to strip
    try:
        return tax_bill_number_header.next().text().strip()
    except Exception:
        return None
