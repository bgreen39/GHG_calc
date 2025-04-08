# GHG Emissions Calculations for Residential Gas
# Include units for thousand cubic feet, and therms 

# Carbon Dioxide (CO2) Emissions
def gas_emissions_co2(value, unit="kwh", output_unit="metric_tons"):
    # Emissions factor in kg CO2 per kWh (352 kg/MWh = 0.352 kg/kWh)
    co2_EF = 0.352

    if unit == "mwh":
        value *= 1000  # convert MWh to kWh

    emissions_kg = value * co2_EF
    emissions = emissions_kg / 1000 if output_unit == "metric_tons" else emissions_kg * 0.00110231  # to short tons
    return emissions

# METHANE (CH4) Emissions
# *create definition for this function*
def gas_emissions_ch4(value, unit="kwh","mwh",output_unit="metric_tons","tons"):
#Emissions factor (ef) from kg co2e per kwh
#     *updated from excel (kg co2 per Mwh)
ch42_EF= 0.023
#conversion from mwh to kwh
if unit == "mwh":
  value *= 1000 
#calculate emissions in kg
emissions_kg = value * ef
emissions_metric_tons = emissions_kg / 1000

# Nitrous Oxide (N2O) Emissions
# *create definition for this function*
def gas_emissions_n2o(value, unit="kwh","mwh",output_unit="metric_tons","tons"):
#Emissions factor (ef) from kg co2e per kwh
#     *updated from excel (kg co2 per Mwh)
n2o_EF= 0.003
#conversion from mwh to kwh
if unit == "mwh":
  value *= 1000 
#calculate emissions in kg
emissions_kg = value * ef
emissions_metric_tons = emissions_kg / 1000


