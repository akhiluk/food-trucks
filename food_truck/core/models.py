from django.db import models

# Create your models here.

# We'll create a model to store the details of the food trucks from the CSV file.
# For the purpose of this assignment we'll only need these columns, so the other columns in the CSV file can be ignored.
class FoodTruck(models.Model):
    id = models.IntegerField(primary_key = True, verbose_name = "ID")
    location_id = models.IntegerField(unique = True, null = False, blank = False, verbose_name = "Location ID")
    applicant = models.CharField(max_length = 300, null = False, blank = False, verbose_name = "Applicant")
    facility_type = models.CharField(max_length = 150, null = True, blank = True, verbose_name = "Facility Type")
    location_description = models.CharField(max_length = 450, null = True, blank = True, verbose_name = "Location Description")
    address = models.CharField(max_length = 150, null = False, blank = False, verbose_name = "Address")
    permit = models.CharField(max_length = 25, null = False, blank = False, verbose_name = "Permit")
    status = models.CharField(max_length = 15, verbose_name = "Status")
    food_items = models.CharField(max_length = 1024, verbose_name = "Food Items", null = True, blank = True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        db_table = "food_trucks"
        verbose_name = "Food Truck"
        verbose_name_plural = "Food Trucks"

    def __str__(self):
        return f"{self.applicant} at {self.location_description}, {self.address}"