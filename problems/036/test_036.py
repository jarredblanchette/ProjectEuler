import solution_036


def test_to_bin():
    assert solution_036.to_bin(0) == '0'
    assert solution_036.to_bin(2) == '10'
    assert solution_036.to_bin(77) == '1001101'
    assert solution_036.to_bin(582) == '1001000110'
    assert solution_036.to_bin(5882) == '1011011111010'


def test_palendromic():
    assert solution_036.palendromic('12321') is True
    assert solution_036.palendromic('123') is False
    assert solution_036.palendromic('11') is True
    assert solution_036.palendromic('10101') is True
    assert solution_036.palendromic('1221') is True

