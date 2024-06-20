def isPalindrome(s):
    s = s.lower()
    return s == s[::-1]

try:
    string = input("Enter a string: ")
    if isPalindrome(string):
        print(f"{string} is a palindrome.")
    else:
        print(f"{string} is not a palindrome.")
except ValueError:
    print("Invalid input! Please enter a valid string.")
