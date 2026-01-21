import solution_052


def test_containSameDigits():
    assert bool(solution_052.containSameDigits(1,1)) is True
    assert bool(solution_052.containSameDigits(12,12)) is True
    assert bool(solution_052.containSameDigits(12,21)) is True
    assert bool(solution_052.containSameDigits(1234567890,5678912340)) is True

    assert bool(solution_052.containSameDigits(1112,1211)) is True
    assert bool(solution_052.containSameDigits(11123,13211)) is True

    assert bool(solution_052.containSameDigits(1234567890,567891234)) is False
    assert bool(solution_052.containSameDigits(1234567890,5678912349)) is False
    assert bool(solution_052.containSameDigits(12345,11111)) is False

def test_getMultiples():
    assert set(solution_052.getMultiples(1)) == set([1,2,3,4,5,6]) 
    assert set(solution_052.getMultiples(2)) == set([2,4,6,8,10,12]) 
    assert set(solution_052.getMultiples(10)) == set([10,20,30,40,50,60])
    assert set(solution_052.getMultiples(12)) == set([12,24,36,48,60,72])
    assert set(solution_052.getMultiples(987)) == set([987,987*2,987*3,987*4,987*5,987*6])