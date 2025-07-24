#9  Encapsulation (Protecting Attributes)
class EnergySystem:
    def __init__(self, building_name, energy_consumption, emission_factor):
        self.building_name = building_name
        self._energy_consumption = energy_consumption  # Protected attribute
        self._emission_factor = emission_factor  # Protected attribute

    # Method to access energy consumption safely
    def get_energy_consumption(self):
        return self._energy_consumption

    # Method to calculate carbon footprint
    def calculate_carbon_footprint(self):
        return self._energy_consumption * self._emission_factor

# Example usage:
building = EnergySystem("Building A", 5000, 0.45)
print(f"Energy Consumption (accessed via method): {building.get_energy_consumption()} kWh")
