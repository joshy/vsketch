from vsketch.curves import quadratic_bezier_path

from .data import POINTS_1000

# vsketch.bezier is using quadtratic_bezier_path
# that is why it is directly imported
# very basic test only for lenth
def test_quadratic_bezier_path():
    path = quadratic_bezier_path(
        POINTS_1000[0].real,
        POINTS_1000[0].imag,
        POINTS_1000[1].real,
        POINTS_1000[1].imag,
        POINTS_1000[2].real,
        POINTS_1000[2].imag,
        POINTS_1000[3].real,
        POINTS_1000[3].imag,
        1.
    )
    assert len(path) == 792
