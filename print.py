def get_even_numbers(start, end):
    """Gets all even numbers between start and end (inclusive).

    Args:
        start: The starting number.
        end: The ending number.

    Returns:
        A string of even numbers separated by ", ".
    """
    even_nums = []
    for num in range(start, end + 1):
        if num % 2 == 0:
            even_nums.append(num)
    return ", ".join(map(str, even_nums))


def get_odd_numbers(start, end):
    """Gets all odd numbers between start and end (inclusive).

    Args:
        start: The starting number.
        end: The ending number.

    Returns:
        A string of even numbers separated by ", ".
    """
    even_nums = []
    for num in range(start, end + 1):
        if num % 2 == 1:
            even_nums.append(num)
    return ", ".join(map(str, even_nums))

