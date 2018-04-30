import numpy as np
from numpy import linalg as la


def create_matrix(row=None, column=None):
    if row >= 0 and column >= 0:
        return np.random.randint(100, size=(row, column))
    else:
        raise ValueError('\nPlease input the correct number of row and column!')


def normalize(input_matrix=None):
    mean_matrix = np.mean(input_matrix, axis=1)
    # print(input_matrix)
    # print(mean_matrix)
    for i in range(len(input_matrix)):
        column_number = len(input_matrix[i])
        for j in range(column_number):
            input_matrix[i][j] -= mean_matrix[i]
    return input_matrix


def main():
    # row = int(input('\nPlease input the row: '))
    # column = int(input('\nPlease input the column: '))
    row = 3
    column = 5
    try:
        matrix = create_matrix(row, column)
    except ValueError as e:
        print(e)
    matrix = matrix.astype(float)
    print(matrix)
    matrix = matrix.T
    matrix = normalize(input_matrix=matrix)
    matrix_T = matrix.T
    new_matrix = (1 / column) * (matrix @ matrix_T)
    print(new_matrix)
    val, vector = la.eig(new_matrix)
    print(val)
    print(vector)
    print(vector @ matrix)


if __name__ == '__main__':
    main()
