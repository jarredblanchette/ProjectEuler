import main

def test_factorial():
    assert main.factorial(1) == 1
    assert main.factorial(10) == 3628800
    assert main.factorial(20) == 2432902008176640000
