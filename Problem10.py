#10 Subclass SolarEnergySystem overriding the carbon footprint method (Polymorphism)
class SolarEnergySystem(EnergySystem):
    def __init__(self, building_name, energy_consumption, emission_factor, solar_production):
        # Call the parent class constructor to initialize inherited attributes
        super().__init__(building_name, energy_consumption, emission_factor)
        self.solar_production = solar_production  # new attribute for solar energy production
    
    # Overriding the carbon footprint method to account for solar production
    def calculate_carbon_footprint(self):
        # Access energy consumption from the parent class (inherited attribute)
        net_consumption = self._energy_consumption - self.solar_production
        return net_consumption * self._emission_factor

# Example usage:
solar_building = SolarEnergySystem("Solar Building", 5000, 0.45, 1500)
carbon_footprint = solar_building.calculate_carbon_footprint()

print(f"Adjusted Carbon Footprint (after solar production): {carbon_footprint:.2f} kg CO2")
