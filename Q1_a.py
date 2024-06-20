def EvenOrOdd(a):
    if (a % 2 == 0):
        print(f"{a} is an EVEN number")
    else:
        print(f"{a} is an ODD number")

while True:
    try:
        number = int(input("Enter a number : "))
        EvenOrOdd(number)
        break
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
