# geolocwrapper.py

from geopy.distance import distance, lonlat
from geopy.geocoders import Nominatim
from geopy.exc import GeopyError


class GeoLocWrapper:

    def __init__(self, addr_str=''):
        self.geolocator = Nominatim(user_agent="test-application")     
        self.location = self.geolocator.geocode(addr_str)
        if self.location == None:
            raise GeopyError
        self.pos = (self.location.longitude, self.location.latitude)
    def get_distance_miles(self, pos0, pos1):
        self.one = (pos0.longitude, pos0.latitude)
        self.two = (pos1.longitude, pos1.latitude)
        self.dist_mile = (distance(lonlat(*self.one), lonlat(*self.two)).miles)
        return self.dist_mile

    def get_distance_kilometers(self, pos0, pos1):
        self.one = (pos0.longitude, pos0.latitude)
        self.two = (pos1.longitude, pos1.latitude)
        self.dist_kilo = (distance(lonlat(*self.one), lonlat(*self.two)))
        return (str(self.dist_kilo).split(" "))[0]



