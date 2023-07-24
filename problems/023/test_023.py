import pytest
import main


def test_properFactors():
    assert main.properFactors(28) == [1 , 2 , 4 , 7 , 14]

def test_perfection():
    assert main.perfection(12) > 0
    assert main.perfection(28) == 0
    assert main.perfection(22) < 0
