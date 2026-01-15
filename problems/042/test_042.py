import solution_042


def test_isTriangle():
    isTriangle = solution_042.triangleGenerator()
    assert isTriangle(1) is True
    assert isTriangle(3) is True
    assert isTriangle(6) is True
    assert isTriangle(10) is True
    assert isTriangle(15) is True
    assert isTriangle(21) is True
    assert isTriangle(28) is True
    assert isTriangle(36) is True
    assert isTriangle(55) is True

    assert isTriangle(2) is False
    assert isTriangle(4) is False
    assert isTriangle(5) is False
    assert isTriangle(7) is False
    assert isTriangle(8) is False
    assert isTriangle(9) is False
    assert isTriangle(11) is False
    assert isTriangle(12) is False
    assert isTriangle(54) is False


def test_score_word():
    assert solution_042.score_word('SKY') == 55
    assert solution_042.score_word('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == (26 + 1) * (26 / 2)  # one per letter
    assert solution_042.score_word('QWERTYUIOPASDFGHJKLZXCVBNM') == (26 + 1) * (26 / 2)  # order doesn't matter
    assert solution_042.score_word('AAAAA') == 5
    assert solution_042.score_word('YYYY') == 100
