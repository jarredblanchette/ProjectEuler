import main
from fractions import Fraction

def test_badSimplify():
    assert main.badSimplify(49,97) == [(4,7)]
    assert main.badSimplify(45,94) == [(5,9)]
    assert main.badSimplify(99,88) == []

