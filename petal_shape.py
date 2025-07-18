import maya.cmds as cmds
import random

def create_petal(length=2.0, width=0.5):
    """Creates a NURBS petal by lofting between two slightly varied curves."""
    half_width = width / 2
    half_length = length / 2

    # define 3 control points for each curve (base -> tip)
    def make_curve(y_offset=0.0, randomness=0.1):
        return cmds.curve(
            d=3,
            p=[
                (-half_width, 0 + y_offset, 0),
                (0, random.uniform(-randomness, randomness) + y_offset, half_length),
                (half_width, 0 + y_offset, 0)
            ],
            k=[0, 0, 0, 1, 1, 1]
        )

    # create two curves offset in Y for lofting depth
    curve1 = make_curve(y_offset=-0.05)
    curve2 = make_curve(y_offset=0.05)

    # loft them into a NURBS surface
    petal = cmds.loft(curve1, curve2, ch=False, u=True, c=False, ar=True, d=3, ss=1)[0]

    # delete construction curves to keep the scene clean
    cmds.delete(curve1, curve2)

    return petal
