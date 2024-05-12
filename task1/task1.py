def is_even(value: int) -> bool:
    """
    Check is value even or not, using mod
    :param value: number to check
    :return: True if value is even, False otherwise
    """
    return value % 2 == 0


def is_even_bitwise(value: int) -> bool:
    """
    Check is value even or not, using bitwise
    :param value: number to check
    :return: True if value is even, False otherwise
    """
    return (value & 1) == 0
