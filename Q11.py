def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if num1 <= 0 or num2 <= 0:
        print("Please enter positive integers.")
    else:
        result = gcd(num1, num2)
        print(f"The GCD of {num1} and {num2} is: {result}")

except ValueError:
    print("Invalid input! Please enter valid integers.")
