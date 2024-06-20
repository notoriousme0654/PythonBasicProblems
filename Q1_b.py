def CheckNumber(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

try:
    number = int(input("Enter a number: "))
    result = CheckNumber(number)
    print(f"The number {number} is {result}.")
except ValueError:
    print(f"The number is ZERO")
