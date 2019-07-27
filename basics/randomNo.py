import random
l=[]
n=int(input("enter the number"))
for i in range(n):
    l.append(random.randint(1,30))
    print("randomized list is:",l)