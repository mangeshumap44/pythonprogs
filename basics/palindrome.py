n=input("enter the number")
list=[]
list.append(n)
rev_list=reversed(list)
if reversed(list)== n:
    print("palindrome")
else:
    print("Not palindrome")