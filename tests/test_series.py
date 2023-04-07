import pytest
from math_series.series import fibonacci, lucas, sum_series


def test_fibonacci():
    # Test the first two numbers in the sequence
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

    # Test other numbers in the sequence
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    assert fibonacci(9) == 34

    # Test edge cases
    assert fibonacci(50) == 12586269025
    assert fibonacci(100) == 354224848179261915075
    assert fibonacci(200) == 280571172992510140037611932413038677189525


def test_lucas():
    # Test the first few numbers in the Lucas sequence
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11
    assert lucas(6) == 18
    assert lucas(7) == 29
    assert lucas(8) == 47

    # Test large input values
    assert lucas(20) == 15127
    assert lucas(50) == 28143753123

    # Test edge cases
    assert lucas(0) == 2
    assert lucas(1) == 1

def test_sum_series():
    # Test the fibonacci sequence
    assert sum_series(0) == 0
    assert sum_series(1) == 1
    assert sum_series(2) == 1
    assert sum_series(3) == 2
    assert sum_series(4) == 3
    assert sum_series(5) == 5
    assert sum_series(6) == 8
    
    # Test the lucas sequence
    assert sum_series(0, 2, 1) == 2
    assert sum_series(1, 2, 1) == 1
    assert sum_series(2, 2, 1) == 3
    assert sum_series(3, 2, 1) == 4
    assert sum_series(4, 2, 1) == 7
    assert sum_series(5, 2, 1) == 11
    assert sum_series(6, 2, 1) == 18
    
    # Test a custom series
    assert sum_series(0, 3, 4) == 3
    assert sum_series(1, 3, 4) == 4
    assert sum_series(2, 3, 4) == 7
    assert sum_series(3, 3, 4) == 11
    assert sum_series(4, 3, 4) == 18
    assert sum_series(5, 3, 4) == 29
    assert sum_series(6, 3, 4) == 47
    