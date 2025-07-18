import maya.cmds as cmds
import random
import utils

def create_stem(height=2.0, radius=0.05):
    """Creates a simple NURBS-extruded stem."""
    curve = cmds.curve(d=1, p=[(0, 0, 0), (0, height, 0)])
    circle = cmds.circle(r=radius, normal=(1, 0, 0), sections=6)[0]
    stem = cmds.extrude(circle, curve, ch=False, rn=False, et=2, ucp=1, fpt=1, upn=1)[0]
    cmds.delete(circle, curve)
    return stem

def create_blooming_petal(length=2.0, width=0.5, randomness=0.1, convert_to_poly=True):
    """Creates a petal with blendShape-driven blooming, returns surface or poly."""
    half_width = width / 2
    half_length = length / 2

    def make_curve(mid_z, tip_offset=0.0, name=""):
        return cmds.curve(
            d=3,
            p=[
                (-half_width, 0, 0),
                (0, tip_offset, mid_z),
                (half_width, 0, 0)
            ],
            k=[0, 0, 0, 1, 1, 1],
            name=name
        )

    base_curve = make_curve(mid_z=half_length * 0.4, tip_offset=-0.3, name="petal_base")
    bloom_curve = make_curve(mid_z=half_length * 1.0, tip_offset=0.3, name="petal_bloom")

    blend = cmds.blendShape(bloom_curve, base_curve, name="petal_bloomBlend")[0]

    loft_a = cmds.duplicate(base_curve)[0]
    loft_b = cmds.duplicate(base_curve)[0]
    cmds.move(-0.05, 0, 0, loft_a, r=True)
    cmds.move(0.05, 0, 0, loft_b, r=True)

    lofted = cmds.loft(loft_a, loft_b, ch=False, u=True, c=False, ar=True, d=3, ss=1)[0]
    cmds.delete(loft_a, loft_b)

    if convert_to_poly:
        poly = utils.convert_nurbs_to_poly(lofted, name="petal")
        cmds.delete(lofted)
        return poly, blend, base_curve, bloom_curve

    return lofted, blend, base_curve, bloom_curve
