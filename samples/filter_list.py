
def filter_list(l: list) -> list:
    """Take one mixed list and returns a list with int values

    Args:
        l (list): Given list from User.

    Returns:
        list: New list with int values.
    """
    return [i for i in l if isinstance(i, int)]


if __name__ == "__main__":
    print(filter_list([1, 2, 'a', 'b']))
    print(filter_list([1, 'a', 'b', 0, 15]))
