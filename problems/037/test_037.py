import solution_037


def test_get_trunkated():
    assert solution_037.get_truncated(3797) == {3, 37, 379, 3797, 797, 97, 7}
    assert solution_037.get_truncated(1100) == {1, 11, 110, 1100, 100}

def test_trunkatable_prime():
    assert solution_037.trunkatable_prime(3797) is True
    assert solution_037.trunkatable_prime(23) is True

    assert solution_037.trunkatable_prime(89) is False
    assert solution_037.trunkatable_prime(3491) is False
    assert solution_037.trunkatable_prime(777) is False
