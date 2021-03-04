def matrix(m,n):
    o=[]
    for i in range(m):
        row=[]
        for j in range(n):
             inp = int(input(f"Enter o [{i}][{j}]"))
        row.append(inp)
        o.append(row)
        return o
def sum (A, B):
            output=[]
            for i in range (len(A)):#number of rows
                row=[]
                for j in range (len(A[0])):#numbe of columns
                    row.append(A[i][j]+B[i][j])
                    row.append(row)
                    return output
m=int(input("Enter the value of m\n"))
n=int(input("Enter the value of n\n"))
print("Enter matrix A")
A=matrix(m,n)
print(A)
print("Enter the matrix B")
B=matrix(m,n)
print(B)
s=sum(A,B)
print(s)
