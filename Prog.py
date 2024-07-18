def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Input number
num = 5

# Calculate factorial
fact = factorial(num)

# Print the factorial
print(f"The factorial of {num} is: {fact}")
