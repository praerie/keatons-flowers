import maya.cmds as cmds
import math
import geometry
import utils
from utils import GOLDEN_ANGLE, polar_to_cartesian, jitter

SCALE_FACTOR = 0.25

def generate_flower(petal_count=55, petal_length=2.0, petal_width=0.5, randomness=0.0, use_fibonacci=True):
    cmds.undoInfo(openChunk=True)
    try:
        flower_group = cmds.group(empty=True, name="keaton_flower#")
        stem = geometry.create_stem(height=2.0)
        cmds.parent(flower_group, stem)

        if use_fibonacci:
            petal_count = utils.fibonacci_sequence(10)[-1]

        blend_nodes = []

        for i in range(petal_count):
            angle = i * GOLDEN_ANGLE
            radius = SCALE_FACTOR * math.sqrt(i + 1)

            if randomness:
                angle = jitter(angle, randomness * GOLDEN_ANGLE)

            x, z = polar_to_cartesian(angle, radius)

            petal, blend, base_curve, bloom_curve = geometry.create_blooming_petal(
                length=petal_length, width=petal_width
            )
            cmds.move(x, 0, z, petal)
            cmds.rotate(0, -angle, 0, petal)
            cmds.parent(petal, flower_group)
            blend_nodes.append(blend)

        attr_name = f"{flower_group}.bloom"
        if not cmds.objExists(attr_name):
            cmds.addAttr(flower_group, longName="bloom", min=0, max=1, defaultValue=0, k=True)

        for blend in blend_nodes:
            cmds.connectAttr(attr_name, f"{blend}.petal_bloom")

        return flower_group
    finally:
        cmds.undoInfo(closeChunk=True)
