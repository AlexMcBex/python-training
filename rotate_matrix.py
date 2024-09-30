matrix = [
    [1 ,2, 3, 4, 5],
    [6 ,7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

def rotate_matrix_clockwise(matrix):
    # rotate matrix 90 degrees clockwise
    return[
        list(reversed(col)) for #reverse each tuple (col) and make a list of them
        col in 
        zip(*matrix) # == [(1, 4,7), (2, 5, 8), (3, 6, 9)]
    ]

def rotate_matrix_counter(matrix):
    #rotate matrix 90 degrees counter clockwise
    return[
        list(col) for
        col in
        zip(*matrix)
    ][::-1]

def rotate_matrix_180(matrix):
    # [9, 8, 7]
    # [6, 5, 4]
    # [3, 2, 1]   
    return[
        list(reversed(col)) for 
        col in
        matrix
    ][::-1]

rotated_clock = rotate_matrix_clockwise(matrix)
# [7, 4, 1]
# [8, 5, 2]
# [9, 6, 3]
for row in rotated_clock:
    print(row)

rotated_counter = rotate_matrix_counter(matrix)
# [3, 6, 9]
# [2, 5, 8]
# [1, 4, 7]
# for row in rotated_counter:
#     print(row)

rotated_180 = rotate_matrix_180(matrix)
# [9, 8, 7]
# [6, 5, 4]
# [3, 2, 1]
# for row in rotated_180:
#     print(row)
