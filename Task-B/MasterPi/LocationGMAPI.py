import MySQLdb, json
from CloudDBUtils import CloudDBUtils
from CarSystem import CarSystem

#for Geolocation
import googlemaps
from datetime import datetime

with open("apikey.json", "r") as file:
    data = json.load(file)

API = data["apikey"]
gmaps = googlemaps.Client(key=API)

class LocationGMAPI:
    """
    Class used to aquire Location of User using the Google Map API.
    """
    def __init__(self):
        self.cloud = CloudDBUtils()

    def geoCode(self, user):
        """
        Returns the details of the Location of the Users Booked Car.

        Parameters:
            user: Username of the user who's Car-location is desired to be returned.
        """
        cur = self.cloud.connection
        with cur.cursor() as cursor:
          uid = CarSystem().fetchid(user)[0]
          cursor.execute("SELECT CarID as VALUE FROM CarBooked WHERE UserID=%s", [uid])
          cid = cursor.fetchone()
          cursor.execute("SELECT Location as VALUE FROM Car WHERE CarID=%s", [cid])
          location = cursor.fetchone()[0]
          #print(location)
          geocode_result = gmaps.geocode(location)
        return print(geocode_result)
        

