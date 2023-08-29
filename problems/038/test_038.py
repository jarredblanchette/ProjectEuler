import main


def test_pandigitial():
    assert main.pandigitial(123456789) is True
    assert main.pandigitial(912345678) is True
    assert main.pandigitial(129873456) is True
    assert main.pandigitial(987654321) is True

    assert main.pandigitial(9) is False
    assert main.pandigitial(999999999) is False
    assert main.pandigitial(123456780) is False
    assert main.pandigitial(123456799) is False


def test_stepwise_multiply():
    assert main.stepwise_multiply(192, 3) == 192384576
    assert main.stepwise_multiply(192, 2) == 192384
    assert main.stepwise_multiply(192, 1) == 192

    assert main.stepwise_multiply(123,5) == 123246369492615

    assert main.stepwise_multiply(678,3) == 67813562034


def test_check_candidate():
    assert main.check_candidate(192384576) == 3

    assert main.check_candidate(192384577) == -1
