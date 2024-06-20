def lcm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers.")
    
    max_num = max(a, b)
    while True:
        if max_num % a == 0 and max_num % b == 0:
            return max_num
        max_num += 1

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = lcm(num1, num2)
    print(f"The LCM of {num1} and {num2} is: {result}")

except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"Error: {e}")
