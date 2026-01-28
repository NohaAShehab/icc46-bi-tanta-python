

def add_numbers(num1:int, num2:int) -> int:
    """
    documentation for the function add_numbers
    :param num1: must be int
    :param num2: must be int
    :return: either int or false
    """
    if isinstance(num1, int) and isinstance(num2, int):
        return num1 + num2
    return False

def div_numbers(num1:int, num2:int) -> float:
    """
    documentation for the function div_numbers
    :param num1: int
    :param num2: int, not equal to 0
    :return: float
    """
    if isinstance(num1, int) and isinstance(num2, int) and num2 !=0:
        return num1 / num2
    return False