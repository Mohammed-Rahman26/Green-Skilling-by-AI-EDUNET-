#15 Import Pandas and create a data set and create a Pandas Series for renewable energy sources.
import pandas as pd

# Sample renewable energy sources data
renewable_sources = ["Solar", "Wind", "Hydropower", "Geothermal", "Biomass"]

# Sample green technology project data (for DataFrame)
data = {
    "Project": ["Solar Farm A", "Wind Turbine X", "Hydropower Y", "Solar Roof Z", "Geothermal Plant P"],
    "Technology": ["Solar", "Wind", "Hydropower", "Solar", "Geothermal"],
    "Capacity (MW)": [150, 300, 200, 50, 100],  # Megawatts
    "Cost (Million $)": [200, 400, 350, 100, 250],  # Project cost
    "Location": ["California", "Texas", "Washington", "Nevada", "Idaho"],
    "Completion Year": [2023, 2024, 2022, 2025, 2023]
}
renewable_series = pd.Series(renewable_sources)

# Print the Series
print("Renewable Energy Sources:")
print(renewable_series)
