str = raw_input("enter the string")
str_rev = reversed(str)
if str == str_rev:
    print("String is palindrome")
else:
    print("string is not palindrome")