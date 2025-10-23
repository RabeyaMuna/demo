def add_numbers(a, b):
    return a + b


def fibonacci(n):
    """Return a list of the first n Fibonacci numbers."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
