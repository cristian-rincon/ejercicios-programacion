def split_integers(n):
    """Converts int to list of strings.

    Args:
        n (int): Given integer.

    Returns:
        [list]: list of numbers after split the given int.
    """
    return [int(i) for i in str(n)]


def digital_root(n: int) -> int:
    """[summary]

    Args:
        n (int): Given number.

    Returns:
        int: Sum of all splitted integers.
    """

    numbers_to_sum = split_integers(n)
    result = sum(numbers_to_sum)

    while len(str(result)) >= 2:
        numbers_to_sum = split_integers(result)
        result = sum(numbers_to_sum)

    return result


if __name__ == "__main__":
    print(digital_root(16))
    print(digital_root(163))
