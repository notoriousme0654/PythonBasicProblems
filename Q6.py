def Fibonacci(n):
    fib_series = [0, 1]

    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return fib_series
    
    a = 0
    b = 1
    for _ in range(2, n):
        c = a + b
        fib_series.append(c)
        a = b
        b = c

    return fib_series

try:
    n_terms = int(input("Enter the number of terms for Fibonacci series: "))
    if n_terms <= 0:
        print("Please enter a positive integer.")
    else:
        result = Fibonacci(n_terms)
        print(f"The Fibonacci series up to {n_terms} terms is: {result}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
