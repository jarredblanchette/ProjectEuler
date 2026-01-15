import solution_033
from fractions import Fraction

def test_badSimplify():
    assert solution_033.badSimplify(49,97) == [(4,7)]
    assert solution_033.badSimplify(45,94) == [(5,9)]
    assert solution_033.badSimplify(99,88) == []

