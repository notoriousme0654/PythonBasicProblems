def sum_of_first_n(n):
    return n * (n + 1) // 2

try:
    n = int(input("Enter a positive integer n: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        result = sum_of_first_n(n)
        print(f"The sum of the first {n} natural numbers is: {result}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")

