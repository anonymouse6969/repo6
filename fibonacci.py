
import time

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_non_recursive(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

n = int(input("Enter the position of Fibonacci number: "))

if n < 0:
    print("Enter a non-negative number.")
else:
    start = time.perf_counter()
    result1 = fibonacci_recursive(n)
    time1 = time.perf_counter() - start

    start = time.perf_counter()
    result2 = fibonacci_non_recursive(n)
    time2 = time.perf_counter() - start

    print("Recursive Fibonacci:", result1)
    print("Non-recursive Fibonacci:", result2)
    print("Recursive execution time:", time1, "seconds")
    print("Non-recursive execution time:", time2, "seconds")
