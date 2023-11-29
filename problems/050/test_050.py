import main


#
# def test_sequential_prime_sum():
#     assert main.sequential_prime_sum(41) == [2, 3, 5, 7, 11, 13]
#     # assert main.prime_sum(953) == 21


def test_prime_sum():
    assert main.prime_sum(1, 2) == 2
    assert main.prime_sum(1, 3) == 5
    assert main.prime_sum(1, 4) == 10
    assert main.prime_sum(1, 5) == 17
    assert main.prime_sum(1, 6) == 28
    assert main.prime_sum(1, 7) == 41
    assert main.prime_sum(1, 8) == 58
    assert main.prime_sum(1, 9) == 77 # [2, 3, 5, 7, 11, 13, 17, 19]

    assert main.prime_sum(3, 4) == 5
    assert main.prime_sum(3, 5) == 12
    assert main.prime_sum(3, 6) == 23
    assert main.prime_sum(3, 7) == 36
    assert main.prime_sum(3, 8) == 53
    assert main.prime_sum(3, 9) == 72 # [5, 7, 11, 13, 17, 19]

    assert main.prime_sum(100,105) == 2777 # [541, 547, 557, 563, 569]