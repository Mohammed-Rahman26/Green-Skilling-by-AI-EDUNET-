#7 Methods to calculate carbon footprint and energy savings.
class EnergySystem:
    def __init__(self, building_name, energy_consumption, emission_factor):
        self.building_name = building_name
        self.energy_consumption = energy_consumption  # in kWh
        self.emission_factor = emission_factor  # kg CO2 per kWh
    
    # Method to calculate carbon footprint
    def calculate_carbon_footprint(self):
        return self.energy_consumption * self.emission_factor

    # Method to calculate energy savings (Assume saving 10% for now)
    def calculate_energy_savings(self):
        return self.energy_consumption * 0.10  # 10% savings

# Example usage:
building = EnergySystem("Building A", 5000, 0.45)
carbon_footprint = building.calculate_carbon_footprint()
energy_savings = building.calculate_energy_savings()

print(f"Carbon Footprint: {carbon_footprint} kg CO2")
print(f"Energy Savings: {energy_savings} kWh")
