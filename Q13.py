def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    return sorted(str1) == sorted(str2)

input_str1 = input("Enter the first string: ")
input_str2 = input("Enter the second string: ")

if are_anagrams(input_str1, input_str2):
    print(f"{input_str1} and {input_str2} are anagrams.")
else:
    print(f"{input_str1} and {input_str2} are not anagrams.")
