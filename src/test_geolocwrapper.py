# test_geolocwrapper.py
import unittest

from geolocwrapper import GeoLocWrapper
from geopy.exc import GeopyError

class TestGeoLocWrapper(unittest.TestCase):
    def test_init(self):
        a = GeoLocWrapper()
        gset = a.locating("806 National Ave, Las Vegas, NM 87701")
        self.assertEqual(str(gset), "Lora Shields Building - NMHU, 806, National Avenue, Las Vegas, San Miguel County, New Mexico, 87701, USA")
    def test_init_fail(self):
        a = GeoLocWrapper()
        with self.assertRaises(GeopyError):
            gset = a.locating("8wfjsagbjhfhsajkat")
    def test_miles(self):
        a = GeoLocWrapper()
        pos1 = a.locating("806 National Ave, Las Vegas, NM 87701")
        pos2 = a.locating("215 Grand Ave, Las Vegas, NM 87701")
        gset = a.get_distance_miles(pos1, pos2)
        self.assertEqual(int(gset),int(0.4582092427954895))
    def test_kilometers(self):
        a = GeoLocWrapper()
        pos1 = a.locating("806 National Ave, Las Vegas, NM 87701")
        pos2 = a.locating("215 Grand Ave, Las Vegas, NM 87701")
        gset = a.get_distance_kilometers(pos1, pos2)
        self.assertEqual(int(gset),int(0.737416295637))
if __name__ == '__main__':
    unittest.main()
