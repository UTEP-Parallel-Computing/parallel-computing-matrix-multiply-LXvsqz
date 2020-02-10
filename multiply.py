#!/usr/bin/env python3
import numpy as np
import time
import pymp


#  Alex Vasquez
#  80579070

def genMatrix(size=200, value=10):
    """
    Generates a 2d square matrix of the specified size with the specified values
    """

    matrix = [[value for col in range(0,size)] for row in range(0,size)]

    return matrix



def genMatrix2(size=200, value=5):
    """
    Generates a 2d square matrix of the specified size with the specified values
    """

    matrix = np.asarray([ np.asarray([value for col in range(0,size)]) for row in range(0,size)])

    return matrix



def genMatrix3(size=200, value=0):
    """
    Generates a 2d square matrix of the specified size with the specified values
    """

    matrix = np.asarray([ np.asarray([value for col in range(0,size)]) for row in range(0,size)])

    return matrix





def printSubarray(matrix, size=10):
    """
    Prints the upper left subarray of dimensions size x size of
    the matrix
    """

    for row in range(1, 10):
        for col in range(1, 10):
            print(f'{matrix[row][col]} ' , end='')
        print('')



def multiplyMatrices(matrixA, matrixB):
    """"
    Generate the product of two 2d square matrices with specified values and
    print results along with time of computation
    """

    product_array = genMatrix3() # array of 0 to hold multiplied values

    rowA = len(matrixA) #length of row from matrixA
    rowB = len(matrixB)  # length of row from matrixB
    colB = len(matrixB[0])  # length of col from matrixBf

    start_time = time.time()
    
    for i in range(0, rowA):  # rows of first matrix
        for j in range(0,colB):  # column of matrixB
            for k in range(0,rowB):  # rows of matrixB
            
                product_array[i][j] += matrixA[i][k] * matrixB[k][j]

    total_time = time.time() - start_time  

   
    print(printSubarray(product_array), 10)
    print("Time to multiply: %s", total_time)
    
 
 
 
 
parallel_product_array = pymp.shared.array((200,200),dtype=np.intc) # generate array for parallel computation
 
     
def parallelMultiply(matrixA, matrixB):
    """"
    Generate the product of two 2d square matrices with specified values using
    multiple threads and pyMP
    """
    
    
    length = len(parallel_product_array)
    start_time = time.time()
    
    with pymp.Parallel(8) as p:
        for i in p.range(0, length):  # using same length since only accounting for m*m array
            for j in range(0,length):  
                for k in range(0,length): 
                    parallel_product_array[i][j] += matrixA[i][k] * matrixB[k][j]
                    
    total_time = time.time() - start_time
    print(printSubarray(parallel_product_array),10)
    print("Time to multiply: %s", total_time)


array1 = genMatrix()
array2 = genMatrix2()

print("-------------------------Serial Multiplication------------------------------------------")

#multiplyMatrices(array1,array2)

print("-------------------------Parallel Multiplication----------------------------------------")

parallelMultiply(array1,array2)

# Serial = Approx 18.78 seconds for array size 200

# Parallel = 1 Thread  60.9174s
#            2 Threads 22.6370s
#            4 Threads 19.3492s
#            8 Threads 16.2354





