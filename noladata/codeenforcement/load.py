from datetime import datetime

from django.contrib.gis.geos import Point

from ..soda.api import soda_get_all
from .models import Case


def get_active_pipeline_judgment_cases():
    """
    Load cases from Code Enforcement's Active Pipeline that are open and in
    stage "Judgment"

        https://data.nola.gov/dataset/CE-Active-Pipeline/8pqz-ftzc
    """
    resource_url = 'http://data.nola.gov/resource/8pqz-ftzc.json'
    filters = {
        'o_c': 'Open',
        'stage': '4 - Judgment',
    }
    return soda_get_all(resource_url, filters)


def parse_date(s):
    if not s:
        return None
    try:
        return datetime.strptime(s, '%Y-%m-%dT%H:%M:%S')
    except ValueError:
        try:
            return datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            raise


def parse_case(json_case):
    return Case(
        location=json_case.get('location', None),
        city=json_case.get('city', None),
        state=json_case.get('state', None),
        zipcode=json_case.get('zipcode', None),
        geopin=json_case.get('geopin', None),
        geoaddress=json_case.get('geoaddress', None),
        geom=Point(float(json_case['xpos']), float(json_case['ypos']), srid=3452),
        caseid=json_case['caseid'],
        caseno=json_case['caseno'],
        o_c=json_case['o_c'],
        stage=json_case.get('stage', None),
        statdate=parse_date(json_case.get('statdate', None)),
        keystatus=json_case.get('keystatus', None),
        initinspection=parse_date(json_case.get('initinspection', None)),
        initinspresult=json_case.get('initinspresult', None),
        prevhearingdate=parse_date(json_case.get('prevhearingdate', None)),
        prevhearingresult=json_case.get('prevhearingresult', None),
        casefiled=parse_date(json_case.get('casefiled', None)),
        lastupload=parse_date(json_case.get('lastupload', None)),
    )


def load():
    for case in get_active_pipeline_judgment_cases():
        saved = parse_case(case)
        saved.save()
