import main


def test_isPandigital():
    assert main.isPandigital(n=123456789) is True
    assert main.isPandigital(n=234567891) is True
    assert main.isPandigital(n=345678912) is True
    assert main.isPandigital(n=345967812) is True

    assert main.isPandigital(n=123) is True
    assert main.isPandigital(n=4123) is True

    assert main.isPandigital(n=11) is False
    assert main.isPandigital(n=13) is False

    assert main.isPandigital(n=111111112) is False
    assert main.isPandigital(n=987654311) is False
    assert main.isPandigital(n=807654311) is False


def test_anySharedDigit():
    assert main.anySharedDigit(1, 2) is False
    assert main.anySharedDigit(1111111, 2) is False
    assert main.anySharedDigit(11111111, 22222222222222222222222) is False
    assert main.anySharedDigit(0, 22222222222222222222222) is False
    assert main.anySharedDigit(10, 2) is False

    assert main.anySharedDigit(123456, 78901) is True
    assert main.anySharedDigit(1, 1) is True


def test_remainingDigits():
    assert main.remainingDigits(123) == 6
    assert main.remainingDigits(123456) == 3
    assert main.remainingDigits(1234567) == 2

    assert main.remainingDigits(987) == 6
