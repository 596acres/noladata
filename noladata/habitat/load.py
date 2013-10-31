import geojson
import os

from ..load import get_processed_data_file


def lots_available_for_gardening():
    filename = os.path.join('habitat', 'habitat_lots_available_for_gardening.geojson')
    lots_file = geojson.load(open(get_processed_data_file(filename)))
    for feature in lots_file['features']:
        yield(feature)
