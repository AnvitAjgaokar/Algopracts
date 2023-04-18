row1 = int(input("Enter the number of rows you want in the first matrix: "))
col1 = int(input("Enter the Number of cols you want in the first matrix: "))

arr1 = []
for i in range(row1):
    arr_temp1 =[]
    for j in range(col1):
        print("Enter Element " , end=" ")
        arr_temp1.append(int(input(":")))
    arr1.append(arr_temp1)


row2 = int(input("Enter the number of rows you want in the second matrix: "))
col2 = int(input("Enter the Number of cols you want in the second matrix: "))
arr2 = []
for i in range(row2):
    arr_temp2 =[]
    for j in range(col2):
        print("Enter Element " , end=" ")
        arr_temp2.append(int(input(":")))
    arr2.append(arr_temp2)


result = []

# Creating Function for Matrix Multiplication
def Matrix_mult(array1,array2,array3):
    for i in range(len(arr1)):
        temp =[]
        for j in range(len(arr2[0])):
            sum=0
            for k in range(len(arr2)):
                sum += arr1[i][k]*arr2[k][j]
            temp.append(sum)
        result.append(temp)

    return result

print("The vector Multiplication is:",Matrix_mult(arr1,arr2,result))