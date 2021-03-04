A=[]
print("enter the element::>")
for i in range(3):
    row=[]
    for j in range (3):
        row.append(int(input))
    A.append(row)

print("Display Array in Matrix Form")
for i in range (3):
    for j in  range(3):
        print([i][j],end=" ")
        print()
        B=[]
        print ("Enter the element::>")
        for i in range(3):
            row=[]
        for j in range (3):
            row.append(int(input))
            B.append(row)
print ("Display Array In Matrix Form")    
for i in range(3):
    for j in range (3):
                print([i][j],end=" ")
print()
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range (3):
    for j in range(3):
        for k in range(3):
            result[i][j]+=A[i][k]*B[i][j]
            print ("the resultant matrix is ::>")
            for r in result:
               print (r)

        
