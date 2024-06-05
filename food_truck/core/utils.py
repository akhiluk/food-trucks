from geopy.distance import geodesic
# Distance between two points given their coordinates
# can be found using the Haversine formula,
# but a pre-made method exists in the geopy library, so
# we'll use that.

def find_distance(lat1, long1, lat2, long2):
    return geodesic((lat1, long1), (lat2, long2)).meters