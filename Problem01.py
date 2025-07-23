#1 Find the sustainable city where carbon_footprint should be less than 400 and temperature should be less than 26.
climate_data = [
    {"city": "City A", "temperature": 25, "carbon_footprint": 500},
    {"city": "City B", "temperature": 30, "carbon_footprint": 350},
    {"city": "City C", "temperature": 22, "carbon_footprint": 600},
    {"city": "City D", "temperature": 15, "carbon_footprint": 200},
    {"city": "City E", "temperature": 28, "carbon_footprint": 450},
]
sustainable_cities = [
    data["city"]
for data in climate_data
if data["temperature"] < 26 and data["carbon_footprint"] < 400
]
print(sustainable_cities)
