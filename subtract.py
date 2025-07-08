def subtract(a, b):
    """
    Subtract two numbers and return the result.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number to subtract from the first.

    Returns:
    int or float: The result of the subtraction.
    """
    return a - b

# Example usage
if __name__ == "__main__":
    num1 = 10
    num2 = 5
    result = subtract(num1, num2)
    print(f"The result of subtracting {num2} from {num1} is: {result}")
