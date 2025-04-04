
### ✅ Next: Basic Test Script (`test_calculator.py`)

#Let’s add a simple test to verify the function works:

#```python
from ghg_emissions_calculator.calculator import calculate_emissions

def test_gasoline():
    result = calculate_emissions(100, "gasoline")
    assert round(result["total_mt"], 2) == round(result["CO2_mt"] + result["CH4_mt"] + result["N2O_mt"], 2)
    print("✅ Gasoline emissions test passed!")

if __name__ == "__main__":
    test_gasoline()
