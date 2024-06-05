import pandas as pd
from pathlib import Path
import sqlite3

df = pd.read_csv(str(Path(__file__).parent.parent / 'food-truck-data.csv'))

df.drop(['cnn', 'blocklot', 'block', 'lot', 'X', 'Y', 'Schedule', 'dayshours', 'NOISent', 'Approved'], axis = 1, inplace = True)
df.drop(['Received', 'PriorPermit', 'ExpirationDate', 'Location', 'Fire Prevention Districts'], axis = 1, inplace = True)
df.drop(['Police Districts', 'Supervisor Districts', 'Zip Codes', 'Neighborhoods (old)'], axis = 1, inplace = True)

columns_to_rename = {
    "locationid": "location_id",
    "FacilityType": "facility_type",
    "LocationDescription": "location_description",
    "FoodItems": "food_items"
}

df.rename(columns = columns_to_rename, inplace = True)

connection = sqlite3.connect(str(Path(__file__).parent / 'trucks.db'))

df.to_sql('food_trucks', connection, if_exists = 'append', index = False)

print("Data import done.")