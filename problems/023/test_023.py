import pytest
import solution_23


def test_properFactors():
    assert solution_23.properFactors(28) == [1 , 2 , 4 , 7 , 14]

def test_perfection():
    assert solution_23.perfection(12) > 0
    assert solution_23.perfection(28) == 0
    assert solution_23.perfection(22) < 0
