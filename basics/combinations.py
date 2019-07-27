a=int(input("enter the first no"))
b=int(input("enter the second no"))
c=int(input("enter the third no"))
l=[]
l.append(a)
l.append(b)
l.append(c)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if i!=j & j!=k & k!=i :
                print(l[i],l[j],l[k])