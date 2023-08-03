import main


def test_to_bin():
    assert main.to_bin(0) == '0'
    assert main.to_bin(2) == '10'
    assert main.to_bin(77) == '1001101'
    assert main.to_bin(582) == '1001000110'
    assert main.to_bin(5882) == '1011011111010'


def test_palendromic():
    assert main.palendromic('12321') is True
    assert main.palendromic('123') is False
    assert main.palendromic('11') is True
    assert main.palendromic('10101') is True
    assert main.palendromic('1221') is True

