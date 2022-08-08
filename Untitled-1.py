def matrix_sum(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print('Error! Matrices dimensions are different!')
        return None
    new_matrix = []
    for i in range(len(matrix1)):
        line_tmp = []
        for j in range(len(matrix1[0])):
            line_tmp.append(matrix1[i][j] + matrix2[i][j])
        new_matrix.append(line_tmp)
    return new_matrix