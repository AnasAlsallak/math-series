import pytest
from math_series.series import fibonacci, lucas, sum_series


# Fibonacci Tests

def test_0_fibonacci():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_1_fibonacci():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_2_fibonacci():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_3_fibonacci():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


def test_4_fibonacci():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected


def test_5_fibonacci():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected


def test_6_fibonacci():
    actual = fibonacci(6)
    expected = 8
    assert actual == expected


def test_7_fibonacci():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected


def test_8_fibonacci():
    actual = fibonacci(8)
    expected = 21
    assert actual == expected


def test_9_fibonacci():
    actual = fibonacci(9)
    expected = 34
    assert actual == expected


def test_10_fibonacci():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected


# Lucas Tests

def test_0_lucas():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_1_lucas():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_2_lucas():
    actual = lucas(2)
    expected = 3
    assert actual == expected


def test_3_lucas():
    actual = lucas(3)
    expected = 4
    assert actual == expected


def test_4_lucas():
    actual = lucas(4)
    expected = 7
    assert actual == expected


def test_5_lucas():
    actual = lucas(5)
    expected = 11
    assert actual == expected


def test_6_lucas():
    actual = lucas(6)
    expected = 18
    assert actual == expected


def test_7_lucas():
    actual = lucas(7)
    expected = 29
    assert actual == expected


def test_8_lucas():
    actual = lucas(8)
    expected = 47
    assert actual == expected


def test_9_lucas():
    actual = lucas(9)
    expected = 76
    assert actual == expected


def test_10_lucas():
    actual = lucas(10)
    expected = 123
    assert actual == expected


# sum_series Tests

def test_0_sum_series():
    actual = sum_series(0)
    expected = 0
    assert actual == expected


def test_1_sum_series():
    actual = sum_series(1)
    expected = 1
    assert actual == expected


def test_2_sum_series():
    actual = sum_series(2)
    expected = 1
    assert actual == expected


def test_3_sum_series():
    actual = sum_series(3)
    expected = 2
    assert actual == expected


def test_4_sum_series():
    actual = sum_series(4)
    expected = 3
    assert actual == expected


def test_5_sum_series():
    actual = sum_series(5)
    expected = 5
    assert actual == expected


def test_6_sum_series():
    actual = sum_series(6)
    expected = 8
    assert actual == expected


def test_7_sum_series():
    actual = sum_series(7)
    expected = 13
    assert actual == expected


def test_8_sum_series():
    actual = sum_series(8)
    expected = 21
    assert actual == expected


def test_9_sum_series():
    actual = sum_series(9)
    expected = 34
    assert actual == expected


def test_10_sum_series():
    actual = sum_series(10)
    expected = 55
    assert actual == expected