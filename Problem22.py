#22 Write code for Daily Energy Consumption Analyzer for Smart Building Rooms.

#This code simulates energy consumption data for three rooms in a building over a 24-hour period and provides insights and suggestions based on usage.
import random

energy_data = {
    "Solar Room": [],
    "Tech Lab": [],
    "Library": [],
}

for hour in range(24):
    energy_data["Solar Room"].append(random.uniform(0.5, 1.2))
    energy_data["Tech Lab"].append(random.uniform(1.0, 2.5))
    energy_data["Library"].append(random.uniform(0.3, 0.9))

for room, readings in energy_data.items():
    total = sum(readings)
    print(f"{room} consumed {total:.2f} kWh today.")

for room, readings in energy_data.items():
    peak_hour = readings.index(max(readings))
    print(f"Peak consumption in {room} at hour {peak_hour}.")


def suggest_action(energy):
    if energy > 2.0:
        return "Consider turning off unused devices or using natural light."
    elif energy > 1.0:
        return "Optimize AC or equipment usage."
    else:
        return "Energy usage is within eco-limits."

for room in energy_data:
    print(f"{room}: {suggest_action(max(energy_data[room]))}")
