from rest_framework import serializers
from core.models import FoodTruck

class FoodTruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodTruck
        fields = "__all__"