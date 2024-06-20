def PrimeOrNot(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range (2,num):
            if num%i == 0:
                return False
        return True    
    
try:
    number = int(input("Enter a positive integer: "))
    if number <= 0:
        print("Please enter a positive integer greater than 0.")
    else:
        if PrimeOrNot(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
except ValueError:
    print("Invalid input! Please enter a valid integer.")    