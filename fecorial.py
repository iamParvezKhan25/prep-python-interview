def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)


# Example usage:
n = 5

print(f"Factorial of {n} (iterative): {factorial_iterative(n)}")

print(f"Factorial of {n} (recursive): {factorial_recursive(n)}")

