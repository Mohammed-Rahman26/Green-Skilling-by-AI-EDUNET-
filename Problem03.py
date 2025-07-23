#3 A function to calculate the average carbon footprint using function.
climate_data = [
    {"city": "City A", "temperature": 25, "carbon_footprint": 500},
    {"city": "City B", "temperature": 30, "carbon_footprint": 350},
    {"city": "City C", "temperature": 22, "carbon_footprint": 600},
    {"city": "City D", "temperature": 15, "carbon_footprint": 200},
    {"city": "City E", "temperature": 28, "carbon_footprint": 450},
]
def average_carbon_footprint(data):
    total = sum([d["carbon_footprint"] for d in data])
    return total / len(data)
print(("Average of Carbon Footprints of the cities is :"),average_carbon_footprint(climate_data))
