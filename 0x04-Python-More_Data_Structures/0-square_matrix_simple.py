#!/usr/bin/python3
def calculate_square_matrix(matrix=[]):
    # Create a new matrix of the same size as the input matrix
    square_matrix = [[0 for _ in range(len(row))] for row in matrix]
    
    # Iterate over each element in the input matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Compute the square of the current element and assign it to the corresponding position in the square matrix
            square_matrix[i][j] = matrix[i][j] ** 2
    
    return square_matrix
