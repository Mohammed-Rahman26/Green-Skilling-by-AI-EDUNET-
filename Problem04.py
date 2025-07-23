#4 Use a lambda function with filter() to get cities with a carbon footprint below the threshold.

climate_data = [
    {"city": "City A", "temperature": 25, "carbon_footprint": 500},
    {"city": "City B", "temperature": 30, "carbon_footprint": 350},
    {"city": "City C", "temperature": 22, "carbon_footprint": 600},
    {"city": "City D", "temperature": 15, "carbon_footprint": 200},
    {"city": "City E", "temperature": 28, "carbon_footprint": 450},
]
sustainability_threshold = 400
sustainable_cities = list(filter(lambda city: city["carbon_footprint"] < sustainability_threshold, climate_data))
print("\nSustainable Cities (carbon footprint < 400 kg CO2):")
for city in sustainable_cities:
    print(f"{city['city']} - {city['carbon_footprint']} kg CO2")
