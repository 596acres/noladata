from itertools import ifilter
from pyquery import PyQuery


BASE_TAX_URL = 'http://services.nola.gov/service.aspx?load=treasury&Type=1&TaxBill='


def load_code_lien_information(tax_bill_number):
    """
    Get code lien information, for example:

        http://services.nola.gov/service.aspx?load=treasury&Type=1&TaxBill=39W414211

    Assessor's page:

        http://qpublic9.qpublic.net/la_orleans_display.php?KEY=1847-MONTEGUTST
    """
    d = open_tax_page(tax_bill_number)
    table = get_tax_items_table(d)
    tax_items = parse_tax_items_table(table)
    lien_items = get_tax_items_by_type(tax_items, 'Code Enforcement Lien')
    return lien_items


def open_tax_page(tax_bill_number):
    return PyQuery(url=BASE_TAX_URL + tax_bill_number)


def get_tax_items_table(d):
    # Try to get table by id
    table = d('table#ctl09_RealEstateTaxData')

    # Else try to find a cell in the table and traverse upward
    if not table:
        period_cell = d('td:contains("Period")')
        table = period_cell
        while table and table.not_('table'):
            table = table.parent()
    return table


def get_tax_items_by_type(tax_items, type_str):
    return ifilter(lambda i: i['Type'] == type_str, tax_items)


def parse_tax_items_table(table):
    headers = map(lambda td: td.text.strip(), table('tr:eq(0) td'))

    def to_item(row):
        row_values = map(lambda td: td.text.strip(), row.findall('td'))
        return dict(zip(headers, row_values))

    return [to_item(row) for row in table('tr')[1:]]
