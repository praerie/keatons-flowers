import math
import random

GOLDEN_ANGLE = 137.5  # degrees

def polar_to_cartesian(angle_deg, radius):
    """Convert polar coordinates to Cartesian (X, Z)."""
    angle_rad = math.radians(angle_deg)
    x = radius * math.cos(angle_rad)
    z = radius * math.sin(angle_rad)
    return x, z

def fibonacci_sequence(n):
    """Generate first n Fibonacci numbers (excluding 0)."""
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def jitter(value, amount):
    """Add random noise to a value."""
    return value + random.uniform(-amount, amount)
