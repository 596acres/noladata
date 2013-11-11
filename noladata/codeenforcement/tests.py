import json

from django.test import TestCase

from .load import parse_case


class LoadCaseTestCase(TestCase):

    def test_parse_case(self):
        json_response = """
        {
            "initinspection": "2013-09-18T10:37:00",
            "prevhearingdate": "2013-11-07T09:15:00",
            "location": "1823 Bodenger Blvd",
            "state": "LA",
            "geoaddress": "1725 Bodenger Blvd",
            "stage": "4 - Judgment",
            "city": "New Orleans",
            "initinspresult": "Violation: No WIP",
            "o_c": "Open",
            "ypos": "525098.33557",
            "prevhearingresult": "Guilty: Public Nuisance",
            "caseid": "180763",
            "geopin": "41000265",
            "zipcode": "70114",
            "statdate": "2013-11-07T09:15:00",
            "caseno": "13-07898-MPM",
            "keystatus": "A hearing was held on 11/07/2013 with a result of 'Guilty: Public Nuisance'.",
            "xpos": "3688393.66638",
            "casefiled": "2013-09-16T11:51:43",
            "lastupload": "2013-11-07T23:00:19"
        }
        """
        json_case = json.loads(json_response)
        case = parse_case(json_case)

        # Test any property for sanity's sake
        self.assertEqual(case.caseid, '180763')

        # Test a year
        self.assertEqual(case.casefiled.year, 2013)
