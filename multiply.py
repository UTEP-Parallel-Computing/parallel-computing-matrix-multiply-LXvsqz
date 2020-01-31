# The number of columns in matrix one must be the same as the number of rows in matrix 2
# undefined if they are not the same.

#!/usr/bin/env python3
import argparse
import numpy as np

# Testing if github works, first commit

def genMatrix(size=3, value=5):
    """
    Generates a 2d square matrix of the specified size with the specified values
    """

    matrix = [[value for col in range(0,size)] for row in range(0,size)]

    return matrix

def genMatrix2(size=3, value=3):
    """
    Generates a 2d square matrix of the specified size with the specified values
    """

    matrix = np.asarray([ np.asarray([value for col in range(0,size)]) for row in range(0,size)])

    return matrix
def genMatrix3(size=3, value=0):
    """
    Generates a 2d square matrix of the specified size with the specified values
    """

    matrix = np.asarray([ np.asarray([value for col in range(0,size)]) for row in range(0,size)])

    return matrix


def getRowLength(ArrayX):
    return len(ArrayX)

def getColLength(ArrayX):
    return len(ArrayX[0])


def multiplyMatrices(matrixA, matrixB):
    #multiply the elements of each row of matrixA by the elements of each column in matrixB
    #elements of each column in the second matrix

    """"
    Generate the product of two 2d square matrices with specified values
    """

    product_array = genMatrix3()  # array of 0s

    rowA = getRowLength(matrixA)
    rowB = getRowLength(matrixB)
    colB = getColLength(matrixB)

    for i in range(0, rowA):  # rows of first matrix
        for j in range(0,colB):  # column of matrixB
            for k in range(0,rowB):  # rows of matrixB
                product_array[i][j] += matrixA[i][k] * matrixB[k][j]

    return product_array


array1 = genMatrix()
array2 = genMatrix2()

print(multiplyMatrices(array1, array2))
