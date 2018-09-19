# test_geolocwrapper.py
import unittest

from geolocwrapper import GeoLocWrapper
from geopy.exc import GeopyError

class TestGeoLocWrapper(unittest.TestCase):
    """A collection of unit tests for the BabySet class. 
    Used to demonstrate and introduce unit testing in Python.
    Related docs: https://docs.python.org/3/library/unittest.html
    """
    def test_init(self):
        """Unit test for GeoLocWrapper constructor."""
        gset = GeoLocWrapper("806 National Ave, Las Vegas, NM 87701")
        self.assertEqual(str(gset.location), "Lora Shields Building - NMHU, 806, National Avenue, Las Vegas, San Miguel County, New Mexico, 87701, USA")
    def test_init_fail(self):
        """Unit test for GeoLocWrapper constructor."""
        with self.assertRaises(GeopyError):
            gset = GeoLocWrapper("8wfjsagbjhfhsajkat")
    def test_miles(self):
        gset = GeoLocWrapper("806 National Ave, Las Vegas, NM 87701")
        pos0 = gset.location
        gset = GeoLocWrapper("215 Grand Ave, Las Vegas, NM 87701")
        pos1 = gset.location
        gset1 = gset.get_distance_miles(pos0, pos1)
        self.assertEqual(gset1,0.4582092427954895)
    def test_kilometers(self):
        gset = GeoLocWrapper("806 National Ave, Las Vegas, NM 87701")
        pos0 = gset.location
        gset = GeoLocWrapper("215 Grand Ave, Las Vegas, NM 87701")
        pos1 = gset.location
        gset1 = gset.get_distance_kilometers(pos0, pos1)
        self.assertEqual(gset1,"0.737416295637")
if __name__ == '__main__':
    unittest.main()
