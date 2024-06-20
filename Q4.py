def factors(num):
    factors = []
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
    return factors

try:
    number = int(input("Enter a positive integer: "))
    if number <= 0:
        print("Please enter a positive integer.")
    else:
        result = factors(number)
        print(f"The factors of {number} are: {result}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")

