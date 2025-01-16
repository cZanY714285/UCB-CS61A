def twenty_twenty_two():
    """Come up with the most creative expression that evaluates to 2022,
    using only numbers and the +, *, and - operators.

    >>> twenty_twenty_two()
    2022
    """
    total = 0

    for i in range(1,101):
        total += i
    total *= 0.4

    return int(total) + 2