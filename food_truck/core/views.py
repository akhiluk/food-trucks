from django.db.models import Q
from rest_framework import generics
from rest_framework.response import Response
from core.models import FoodTruck
from core.serializers import FoodTruckSerializer
from core.utils import find_distance
from rest_framework import status

# Create your views here.
def get_food_trucks():
    # We're using Q here, since the filter() method performs a SQL 'AND', and not an 'OR'
    # With Q, we can pass an 'OR' condition to the ORM.
    return FoodTruck.objects.filter(facility_type = 'Truck').filter(Q(status = 'ISSUED') | Q(status = 'APPROVED')).order_by('location_id')

class FoodTruckList(generics.ListAPIView):
    queryset = get_food_trucks()
    serializer_class = FoodTruckSerializer

class NearestFoodTrucks(generics.GenericAPIView):
    queryset = get_food_trucks()
    serializer_class = FoodTruckSerializer

    def post(self, request, *args, **kwargs):
        try:
            input_latitude = float(request.data.get("latitude"))
            input_longitude = float(request.data.get("longitude"))
        except (TypeError, ValueError):
            return Response({
                "error": "Latitude and Longitude are required, and should be of floating-type."
            }, status = status.HTTP_400_BAD_REQUEST)
        
        food_trucks = get_food_trucks()
        food_trucks_with_distance = []

        for truck in food_trucks:
            distance = find_distance(input_latitude, input_longitude, truck.latitude, truck.longitude)
            food_trucks_with_distance.append((truck, distance))
        
        nearest_food_trucks = sorted(food_trucks_with_distance, key = lambda x: x[1])[:10]

        serializer_data = [item[0] for item in nearest_food_trucks]
        serializer = self.get_serializer(serializer_data, many = True)

        return Response(serializer.data)