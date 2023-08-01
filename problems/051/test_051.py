import main


def test_familyGenerator():
    assert set(main.family_generator(13, [0])) == set([3, 13, 23, 33, 43, 53, 63, 73, 83, 93])
    assert set(main.family_generator(566003, [3, 4])) == set([566003, 566113, 566223, 566333, 566443, 566553, 566663, 566773, 566883, 566993])
    assert set(main.family_generator(123, [2, 0])) == set([20, 121, 222, 323, 424, 525, 525, 626, 727, 828, 929])
