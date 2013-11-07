

def format_street_address(house_number=None, street_dir=None, street_name=None,
                          street_type=None):
    """
    Format the pieces of a street address into a standard street address.
    """
    return ' '.join([str(p) for p in (house_number, street_dir, street_name, street_type) if p])
