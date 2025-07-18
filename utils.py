import maya.cmds as cmds
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

def convert_nurbs_to_poly(nurbs_obj, name=None, divisions=6):
    """
    Converts a NURBS surface to a polygon mesh.
    Returns the poly object name.
    """
    poly = cmds.nurbsToPoly(
        nurbs_obj,
        mnd=1,  # quads
        ch=False,
        f=2,    # per span # of isoparms
        pt=1,   # uniform parameterization
        ut=divisions,
        vt=divisions,
        name=name or f"{nurbs_obj}_poly"
    )[0]
    return poly
