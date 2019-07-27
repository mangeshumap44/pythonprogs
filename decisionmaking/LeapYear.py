num=input("Enter year")
if num%4==0:
    print("Year is Leap Year")
elif num%400==0:
    print("This is Leap Year")
else:
    print("This is not Leap Year")