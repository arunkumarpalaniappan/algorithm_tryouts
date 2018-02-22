def matrixZero(matrix):
    tMatrix = [row[:] for row in matrix]
    for index in range(0,len(matrix)):
        for secondaryIndex in range(0,len(matrix[index])):
            if tMatrix[index][secondaryIndex] == 0:
                for tindex in range(0,len(matrix)):
                    matrix[tindex][secondaryIndex] = 0
                for tindex in range(0,len(matrix)):
                    matrix[index][tindex] = 0
    return matrix

print matrixZero([[0,1,2,3],[2,3,6,7],[8,9,3,4],[4,5,6,0]])