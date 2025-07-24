# 8
# Subclass SolarEnergySystem inheriting from EnergySystem.
class SolarEnergySystem(EnergySystem):
    def __init__(self, building_name, energy_consumption, emission_factor, solar_production):
        # Inherit attributes from the parent class
        super().__init__(building_name, energy_consumption, emission_factor)
        self.solar_production = solar_production  # energy produced by solar panels in kWh
    
    # Method to calculate net energy consumption (energy used - solar energy produced)
    def net_energy_consumption(self):
        return self.energy_consumption - self.solar_production

# Example usage:
solar_building = SolarEnergySystem("Solar Building", 5000, 0.45, 1500)
net_consumption = solar_building.net_energy_consumption()

print(f"Net Energy Consumption: {net_consumption} kWh")
