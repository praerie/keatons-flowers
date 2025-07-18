import maya.cmds as cmds
import math
import petal_shape
import utils
from utils import GOLDEN_ANGLE, polar_to_cartesian, jitter

SCALE_FACTOR = 0.25   # controls petal spacing in spiral

def generate_fibonacci_sequence(n):
    """Returns the first `n` Fibonacci numbers (excluding 0)."""
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def generate_flower(
    petal_count=55,
    petal_length=2.0,
    petal_width=0.5,
    randomness=0.0,
    use_fibonacci=True
):
    """Creates a spiral flower with petals arranged using the golden angle."""
    cmds.undoInfo(openChunk=True)
    try:
        flower_group = cmds.group(empty=True, name="keaton_flower#")

        if use_fibonacci:
            petal_count = utils.fibonacci_sequence(10)[-1]  

        for i in range(petal_count):
            angle = i * GOLDEN_ANGLE
            radius = SCALE_FACTOR * math.sqrt(i + 1)

            if randomness:
                angle = jitter(angle, randomness * GOLDEN_ANGLE)

            x, z = polar_to_cartesian(angle, radius)

            # create and position petal
            petal = petal_shape.create_petal(petal_length, petal_width)
            cmds.move(x, 0, z, petal)
            cmds.rotate(0, -angle, 0, petal)
            cmds.parent(petal, flower_group)

        return flower_group
    finally:
        cmds.undoInfo(closeChunk=True)
