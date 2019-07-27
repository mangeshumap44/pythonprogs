x=[[1,2,3],
   [4,5,6],
   [7,8,9]]
y=[[7,8,9],
   [2,3,4],
   [5,6,7]]
Multiplication=[[0,0,0],
               [0,0,0],
               [0,0,0]]
for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            Multiplication[i][j]=Multiplication[i][j]+x[i][k]*y[k][j]
print(Multiplication)