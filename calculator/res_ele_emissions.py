# Calculations for GHG emissions from Electrical Consumption

# Define calculation emissions for electrical consumption.
# Make sure to include calculations for these different units: kilowatt hours and megawatt hours
# Note: In guidebook note that users can request units to be added. Look up EFs to use for the ghg emissions calculations.

# Carbon Dioxide (CO2) Emissions
def electricity_emissions(value, unit="kwh","mwh",output_unit="metric_tons","tons"):

#Emissions factor (ef) from kg co2e per kwh
ef=0.4
#conversion from mwh to kwh
if unit == "mwh":
  value *= 1000 

#calculate emissions in kg
emissions_kg = value * ef
emissions_metric_tons = emissions_kg / 1000



# Methane (CH4) Emissions
# *create definition for this function*

# Nitrous Oxide (N2O) Emissions
# *create definition for this function*
