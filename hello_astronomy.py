# My first tracked Python file
import numpy as np

def calculate_distance(parallax_arcsec):
    """Calculate distance from parallax."""
    return 1.0 / parallax_arcsec

# Test with Proxima Centauri
distance = calculate_distance(0.768)
print(f"Distance to Proxima Centauri: {distance:.2f} parsecs")