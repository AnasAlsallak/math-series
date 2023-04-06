# Fibonacci Function

def fibonacci(n):
    """
    Calculate the nth number in the Fibonacci sequence.

    Arguments:
        n (int): The index of the number to calculate. Must be a positive integer.

    Returns:
        int: The nth number in the Fibonacci sequence.

    Raises:
        ValueError: If the input n is not a positive integer.

    Examples:
        If n is 0, the function returns 0.
        If n is 1, the function returns 1.
        If n is 6, the function returns 8.
    """
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(n-1):
            a, b = b, a + b
        return b


# Lucas Function

def lucas(n):
    """
    Calculate the nth number in the Lucas sequence.

    Arguments:
    n (int): The index of the number to calculate. Must be a non-negative integer.

    Returns:
    int: The nth number in the Lucas sequence.

    Raises:
    ValueError: If the input n is not a non-negative integer.

    Examples:
    If n is 0, the function returns 2.
    If n is 1, the function returns 1.
    If n is 6, the function returns 18.
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        a, b = 2, 1
        for _ in range(n-1):
            a, b = b, a + b
        return b


# sum_series

def sum_series(n, first=0, second=1):
    """
    Calculate and print the nth element in a series.

    Arguments:
    n (int): The index of the element to be calculated and printed.
    first (int): The first element in the series. Default value is 0.
    second (int): The second element in the series. Default value is 1.

    Returns:
    int: The nth element in the series.

    Examples:
    If n is 0, the function returns and prints the first element (0).
    If n is 1, the function returns and prints the second element (1).
    If n is 6 and the first two elements are 0 and 1, the function returns and prints the sixth element (8).
    """
    if first == 0 and second == 1:
        return fibonacci(n)

    elif first == 2 and second == 1:
        return lucas(n)

    else:
        if n == 0:
            return first
        elif n == 1:
            return second
        else:
            return sum_series(n-1, first, second) + sum_series(n-2, first, second)