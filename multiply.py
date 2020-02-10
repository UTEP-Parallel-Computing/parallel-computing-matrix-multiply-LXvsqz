#!/usr/bin/env python3
import numpy as np
import time
import pymp


#  Alex Vasquez
#  80579070

def genMatrix(size=200, value=5):
    """
    Generates a 2d square matrix of the specified size with the specified values
    """

    matrix = [[value for col in range(0,size)] for row in range(0,size)]

    return matrix

def genMatrix2(size=200, value=3):
    """
    Generates a 2d square matrix of the specified size with the specified values
    """

    matrix = np.asarray([ np.asarray([value for col in range(0,size)]) for row in range(0,size)])

    return matrix
def genMatrix3(size=200, value=100):
    """
    Generates a 2d square matrix of the specified size with the specified values
    """

    matrix = np.asarray([ np.asarray([value for col in range(0,size)]) for row in range(0,size)])

    return matrix

testArray = pymp.shared.array((200,200),dtype=np.intc)



def printSubarray(matrix, size=10):
    """
    Prints the upper left subarray of dimensions size x size of
    the matrix
    """

    for row in range(1, 10):
        for col in range(1, 10):
            print(f'{matrix[row][col]} ' , end='')
        print('')


def getRowLength(ArrayX):
    return len(ArrayX)

def getColLength(ArrayX):
    return len(ArrayX[0])


def multiplyMatrices(matrixA, matrixB):

    """"
    Generate the product of two 2d square matrices with specified values and
    print results along with time of computation
    """

    product_array = genMatrix3() # array of 0 to hold multiplied values

    rowA = getRowLength(matrixA)  # length of row from matrixA
    rowB = getRowLength(matrixB)  # length of row from matrixB
    colB = getColLength(matrixB)  # length of col from matrixBf

    start_time = time.time()
    
    for i in range(0, rowA):  # rows of first matrix
        for j in range(0,colB):  # column of matrixB
            for k in range(0,rowB):  # rows of matrixB
                product_array[i][j] += matrixA[i][k] * matrixB[k][j]

    total_time = time.time() - start_time  

    print(printSubarray(product_array), 10)
    print("Time to multiply: %s", total_time)
    
    
def parallelMultiply(matrixA, matrixB, matrixC):
    with pymp.Parallel(4) as p:
       print("Hello from thread {} of {}".format(p.thread_num, p.num_threads)) 
    
    
    
    
def testParallel():
    with pymp.Parallel(4) as p:
        print("Hello from thread {} of {}".format(p.thread_num, p.num_threads))



array1 = genMatrix()
array2 = genMatrix2()



multiplyMatrices(array1, array2)
#testParallel()
