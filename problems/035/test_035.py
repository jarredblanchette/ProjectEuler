import solution_035


def test_rotate():
    assert set(solution_035.rotate(197)) == set([197, 971, 719])
    assert set(solution_035.rotate(1234)) == set([1234, 2341, 3412, 4123])
