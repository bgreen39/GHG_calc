# testing electricty emissions functions
print(calculate_electricity_emissions(500, unit="MWh"))  # Should return emissions in metric tons
print(calculate_electricity_emissions(500, unit="MWh", output_unit="tons"))  # Should return emissions in U.S. tons
print(calculate_electricity_emissions(1000, unit="kWh"))  # Emissions for 1000 kWh
print(calculate_electricity_emissions(1, unit="MWh"))  # Emissions for 1 MWh
print(calculate_electricity_emissions(1, unit="kWh"))  # Emissions for 1 kWh
