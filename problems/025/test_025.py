import pytest
import main


def test_fib():
    assert main.fib(1) == 1
    assert main.fib(5) == 5
    assert main.fib(7) == 13
    assert main.fib(12) == 144
    assert main.fib(30) == 832040
