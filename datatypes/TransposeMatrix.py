x=[[1,2,3],
   [4,5,6]]
Transpose=[[0,0,],
           [0,0,],
           [0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        Transpose[j][i]=x[i][j]
print(Transpose)