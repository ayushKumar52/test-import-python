# Example function to add two numbers
def add(a, b):
    result = a + b
    print(f"Adding {a} and {b} results in {result}.")
    return result

# Example function to subtract two numbers
def subtract(a, b):
    result = a - b
    print(f"Subtracting {b} from {a} results in {result}.")
    return result

# Example function to multiply two numbers
def multiply(a, b):
    result = a * b
    print(f"Multiplying {a} and {b} results in {result}.")
    return result

# Example function to divide two numbers
def divide(a, b):
    if b == 0:
        print("Division by zero is not allowed.")
        return None
    result = a / b
    print(f"Dividing {a} by {b} results in {result}.")
    return result

# Example usage
if __name__ == "__main__":
    add(10, 5)
    subtract(10, 5)
    multiply(10, 5)
    divide(10, 5)
    divide(10, 0)
