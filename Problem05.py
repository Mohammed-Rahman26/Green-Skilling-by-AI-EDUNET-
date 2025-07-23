#5 Use max() to find the city with the highest carbon footprint
climate_data = [
    {"city": "City A", "temperature": 25, "carbon_footprint": 500},
    {"city": "City B", "temperature": 30, "carbon_footprint": 350},
    {"city": "City C", "temperature": 22, "carbon_footprint": 600},
    {"city": "City D", "temperature": 15, "carbon_footprint": 200},
    {"city": "City E", "temperature": 28, "carbon_footprint": 450},
]
highest_footprint_city = max(climate_data, key=lambda city: city["carbon_footprint"])
print(f"\nCity with the highest carbon footprint:")
print(f"{highest_footprint_city['city']} - {highest_footprint_city['carbon_footprint']} kg CO2")
