"""Develop a MapReduce program to implement Matrix Multiplication"""

from functools import reduce

def mapper(matrix1, matrix2):
    key_value_pairs = []

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                key_value_pairs.append(((i, j), matrix1[i][k] * matrix2[k][j]))

    return key_value_pairs


def reducer(key, values):
    return sum(values)


def map_reduce(matrix1, matrix2):
    key_value_pairs = mapper(matrix1, matrix2)

    grouped_values = {}

    for key, value in key_value_pairs:
        if key not in grouped_values:
            grouped_values[key] = []

        grouped_values[key].append(value)

    result = {}

    for key in grouped_values:
        result[key] = reducer(key, grouped_values[key])

    return result


def result_to_matrix(result, rows, cols):
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for key, value in result.items():
        matrix[key[0]][key[1]] = value

    return matrix


matrix1 = [[1, 2, 3],
           [4, 5, 6]]

matrix2 = [[7, 8],
           [9, 10],
           [11, 12]]

result = map_reduce(matrix1, matrix2)

result_matrix = result_to_matrix(
    result,
    len(matrix1),
    len(matrix2[0])
)

for row in result_matrix:
    print(row)