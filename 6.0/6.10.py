def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = 4
result = fibonacci(n)
print(f"The {n}th term of the Fibonacci sequence is:", result)