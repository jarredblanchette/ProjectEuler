import pytest
import solution_25


def test_fib():
    assert solution_25.fib(1) == 1
    assert solution_25.fib(5) == 5
    assert solution_25.fib(7) == 13
    assert solution_25.fib(12) == 144
    assert solution_25.fib(30) == 832040
