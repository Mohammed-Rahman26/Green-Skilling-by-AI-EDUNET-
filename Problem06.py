#6 Define the EnergySystem class.
class EnergySystem:
    def __init__(self, building_name, energy_consumption, emission_factor):
        self.building_name = building_name
        self.energy_consumption = energy_consumption  # in kWh
        self.emission_factor = emission_factor  # kg CO2 per kWh

building = EnergySystem("Building A", 5000, 0.45)
print(f"{building.building_name}: {building.energy_consumption} kWh, {building.emission_factor} kg CO2/kWh")
