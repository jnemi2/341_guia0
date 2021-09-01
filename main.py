def factorial(integer):
    """
    :type integer: int
    """
    result = 1
    for i in range(1, integer+1):
        result = i * result
    return result


def recursive_factorial(integer):
    if integer <= 1:
        return 1
    return integer * factorial(integer - 1)


print(factorial(7))
print(recursive_factorial(7))
