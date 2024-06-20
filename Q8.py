def Sum_of_digits(number):
    sum_digits = 0
    
    while number > 0:
        sum_digits = sum_digits + number % 10
        number = number // 10
    return sum_digits

try:
    number = int(input("Enter a number: "))
    result = Sum_of_digits(number)
    print(f"The sum of digits of {number} is {result}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")