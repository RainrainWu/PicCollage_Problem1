"""
PicCollage_Problem1.problem1.problem1 contains the function for caculating
how many numbers contains a token in a range from 1 to N.
"""


def contain_sevens(number: int = 1000, token: int = 7, /) -> int:
    """
    contains_sevens caculates how many numbers contains a token in a range
    from 1 to N. Implements via looping a generator and add counter by 1
    if current element contains the token.

    Args:
        number (int): the upperbound of the range, default is 1000.
        token (int): the token to be checked.

    Returns:
        Int: the total amount of numbers that contains the token, got -1 if
        encounter any exception.
    """

    try:
        gen = range(1, int(number) + 1)
    except ValueError:
        print("Failed to construct generator, please check your number")
        return -1

    token_str = str(token)
    count = 0
    for i in gen:
        if token_str in str(i):
            count += 1
    return count


if __name__ == '__main__':
    print(contain_sevens("1000"))
