def addmultiplenumbers(numbers):
    """Return the sum of a list of numbers."""
    return sum(numbers)


def multiplymultiplenumbers(numbers):
    """Return the product of a list of numbers."""
    product = 1
    for number in numbers:
        product *= number
    return product


def isiteven(num):
    """Return True if num is an even whole number, otherwise False."""
    if isinstance(num, bool):
        return False
    if not isinstance(num, (int, float)):
        return False
    if num != int(num):
        return False
    return int(num) % 2 == 0


def isitaninteger(num):
    """Return True if num is an integer value, otherwise False."""
    if isinstance(num, bool):
        return False
    if not isinstance(num, (int, float)):
        return False
    return num == int(num)


def main():
    print("Hello learners!")
    print("This calculator supports addmultiplenumbers, multiplymultiplenumbers, isiteven, and isitaninteger.")


if __name__ == "__main__":
    main()
