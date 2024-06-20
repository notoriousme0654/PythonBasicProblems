def isArmstrong(number):
    number_of_digits = len(str(number))
    sum_of_powers = 0
    temp = number
    
    while temp > 0:
        digit = temp % 10
        sum_of_powers = sum_of_powers + (digit ** number_of_digits)
        temp = temp // 10
    return number == sum_of_powers

try:
    number = int(input("Enter a number: "))
    if isArmstrong(number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
