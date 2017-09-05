def matrixRotation(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    else:
        for outerIndex in range(0,len(matrix)/2):
            last = len(matrix) - 1 - outerIndex
            for innerIndex in range(outerIndex,last):
                offset = innerIndex - outerIndex
                top = matrix[outerIndex][innerIndex]
                matrix[outerIndex][innerIndex] = matrix[last-offset][outerIndex]
                matrix[last-offset][outerIndex] = matrix[last][last-offset]
                matrix[last][last-offset] = matrix[outerIndex][last]
                matrix[outerIndex][last] = top
        return matrix


print matrixRotation([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]) # O(N^2)