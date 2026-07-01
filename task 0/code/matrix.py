array1 = [[1 ,2],
          [3,4]]

array2 = [[5 , 6],
          [7 ,8]
        ] 


def matrix_sum(array1, array2):
    result = []
    
    for i in range(len(array1)):
        Row_result = []
    
        for j in range(len(array1[0])):
    
            Row_result.append(array1[i][j] + array2[i][j])
    
        result.append(Row_result)
    
    return result 


def matrix_sub(array1, array2):
    
    result = []
    for i in range(len(array1)):
    
        Row_result = []
    
        for j in range(len(array1[0])):
    
            Row_result.append(array1[i][j] - array2[i][j])
        result.append(Row_result)
    
    return result 


def matrix_multiplication(array1, array2):
    result = []
    
    for i in range(len(array1)):
    
        Row_result = []
        for j in range(len(array2[0])):
    
            sum_val = 0
            for k in range(len(array2)):
    
                sum_val += array1[i][k] * array2[k][j]
    
            Row_result.append(sum_val)
        result.append(Row_result)
    
    return result 


def scalarsum(scalar, arr):
    result = []
    
    for i in range(len(arr)):
        Row_result = []
        for j in range(len(arr[0])):
    
            Row_result.append(arr[i][j] + scalar)
        result.append(Row_result)
    
    return result


def scalarsub(scalar, arr):
    result = []
    for i in range(len(arr)):
        Row_result = []
    
        for j in range(len(arr[0])):
            Row_result.append(arr[i][j] - scalar)
    
        result.append(Row_result)
    return result



def matnorm(arr):

    flat = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            flat.append(arr[i][j])


    min_val = flat[0]
    max_val = flat[0]


    for val in flat:
        if val < min_val:

            min_val = val

        if val > max_val:

            max_val = val

    result = []
    for i in range(len(arr)):
        Row_result = []

        for j in range(len(arr[0])):
           
            norm_val = (arr[i][j] - min_val) / (max_val - min_val)

            Row_result.append(norm_val)

        result.append(Row_result)

    return result


# here I make a test for every function using the 2 matrices mentioned 
print("Matrix Sum =", matrix_sum(array1, array2))
print("Matrix Sub =", matrix_sub(array1, array2))
print("Matrix Mul =", matrix_multiplication(array1, array2))
print("Scalar Sum =", scalarsum(2, array1))
print("Scalar Sub =", scalarsub(1, array1))
print("Matrix Normalization =", matnorm(array1))