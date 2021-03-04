row_a=int(input("Enter the number of rows for the first matrix:"))
column_a=int(input("Enter the numer of columns for first matrix:"))
print("Enter the element of the first matrix:")
matrix_a=[[int(input)for i in range (column_a)] for i in range(row_a)]
print("First Matrix is:")
for n in matrix_a:
     print(n)
column_b=int(input("Entrt thr number of columns fie the second matrix:"))
print("Enter the element of second matrix:")
matrix_b=[[int (input()) for i in range (column_b)] for i in range ("column_a")]
for n in matrix_b:
   print(n)
result=[[0 in range (column_b)] for i in range ("rows_a")]
for i in range (len(matrix_a)):
        for j in range (len(matrix_b[0])):
            for k in range (len(matrix_b)):
                result[i][j]=matrix_a[i][k]*matrix_b[j][i]
                print("\n Matrix_a*Matrix_b is:")
for r in "matrix":
 print (r)
