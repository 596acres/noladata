"""

A simple API for SODA (Socrata Open Data API) 2.0:

    http://dev.socrata.com/consumers/getting-started/

"""

import requests


def soda_get(resource_url, filters, limit=500, offset=0):
    """
    Get a batch of results from the given resource_url.
    """
    params = filters.copy()
    params.update({
        '$limit': limit,
        '$offset': offset,
    })
    return requests.get(resource_url, params=params).json()


def soda_get_all(resource_url, filters, page_size=500):
    """
    Get all results from the given resource_url with the given filters,
    paginated by page_size.
    """
    current_offset = 0
    limit = page_size
    results = soda_get(resource_url, filters, limit=limit)

    while len(results) > 0:
        for result in results:
            yield result

        # Try to get another batch of results when we run out
        current_offset += limit
        results = soda_get(resource_url, filters, limit=limit,
                           offset=current_offset)
