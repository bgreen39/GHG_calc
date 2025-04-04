# Transportation Emissions from Diesel Vehicles: units in liters and/or gallons
# Fuel densities in kg/L
fuel_densities = {
    "gasoline": 0.75,
    "diesel": 0.75,
    "ethanol": 0.79,
    "cng": 0.000656
}

# Emission factors in kg of gas per kg of fuel
emission_factors = {
    "gasoline": {"co2": 8.78, "ch4": 0.03, "n2o": 0.02},
    "diesel": {"co2": 10.21, "ch4": 0.01, "n2o": 0.04},
    "ethanol": {"co2": 5.75, "ch4": 0.025, "n2o": 0.015},
    "cng": {"co2": 0.05444, "ch4": 0.001, "n2o": 0.0005}
}

def calculate_emissions(value, fuel_type, unit="gallon", output_unit="metric_tons"):
    if unit == "gallon":
        liters = value * 3.7854  # convert gallons to liters
    else:
        raise ValueError("Unsupported unit. Please input in gallons.")

    if fuel_type not in fuel_densities or fuel_type not in emission_factors:
        raise ValueError(f"Unsupported fuel type: {fuel_type}")

    # Convert volume to mass (kg)
    density = fuel_densities[fuel_type]
    mass_kg = liters * density

    # Get emission factors
    ef = emission_factors[fuel_type]

    # Calculate emissions in kg
    co2_kg = mass_kg * ef["co2"]
    ch4_kg = mass_kg * ef["ch4"]
    n2o_kg = mass_kg * ef["n2o"]

    # Convert to metric tons
    co2_mt = co2_kg / 1000
    ch4_mt = ch4_kg / 1000
    n2o_mt = n2o_kg / 1000

    return {
        "fuel_mass_kg": mass_kg,
        "CO2_mt": co2_mt,
        "CH4_mt": ch4_mt,
        "N2O_mt": n2o_mt,
        "total_mt": co2_mt + ch4_mt + n2o_mt
    }

# Example usage
result = calculate_emissions(100, "gasoline")
print(result)



