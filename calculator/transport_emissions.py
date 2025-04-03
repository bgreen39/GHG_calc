# Transportation Emissions from Diesel Vehicles: units in liters and/or gallons
#          * Emission Factors for Gasoline, Diesel, CNG, and Ethanol Fuel Types *
# Gasoline (in gallons) emissions calculation
def transport_emissions_UNL(value, unit="gallon",output_unit="metric_tons"):
# CO2 emissions factor (EF) kg CO2 per unit (if CO2 is MT CO2 per unit EF=0.00878)
unl_EF= 8.78
# Diesel (in gallons) emissions calculation
def transport_emissions_DSL(value, unit="gallon",output_unit="metric_tons"):
# CO2 emissions factor (EF) kg CO2 per unit (if CO2 is MT CO2 per unit EF=0.01021)
dsl_EF= 10.21
# Compressed Natural Gas or CNG (in scf) emissions calculation
def transport_emissions_CNG (value, unit="gallon",output_unit="metric_tons"):
# CO2 emissions factor (EF) kg CO2 per unit (if CO2 is MT CO2 per unit EF=0.01021)
cng_EF= 0.05444
# Ethanol (in gallons) emissions calculation
def transport_emissions_ETH (value, unit="gallon",output_unit="metric_tons"):
# CO2 emissions factor (EF) kg CO2 per unit (if CO2 is MT CO2 per unit EF=0.01021)
eth_EF= 5.75

#          * Conversions from gallons to kg *
#  get densities for different fuel types!!!!!!!!!!!!!!!
if unit == "gallon":
  value *= 3.8 

# formula for conversion of gallons to kg: volume/value (in gallons) x density (in kg/L) x conversion factor (L/gallon)
#calculate emissions in kg
emissions_kg = value * ef
emissions_metric_tons = emissions_kg / 1000

# gasoline density= 
# diesel density= 0.75 kg/L
# compressed natural gas density= 
# ethanol density= 
