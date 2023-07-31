import main


def test_rotate():
    assert set(main.rotate(197)) == set([197, 971, 719])
    assert set(main.rotate(1234)) == set([1234, 2341, 3412, 4123])
