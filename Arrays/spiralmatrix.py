# https://leetcode.com/problems/spiral-matrix/description/
def go_left_to_right(start_from, go_till, step_over_by, in_row, matrix, arr):
    for i in range(start_from, go_till, step_over_by):
        arr.append(matrix[in_row][i])


def go_top_to_down(start_from, go_till, step_over_by, in_column, matrix, arr):
    for i in range(start_from, go_till, step_over_by):
        arr.append(matrix[i][in_column])
        matrix[i].pop(in_column)


def right_to_left(start_from, go_till, step_over_by, in_row, matrix, arr):
    for i in range(start_from, go_till, step_over_by):
        arr.append(matrix[in_row][i])


def down_to_top(start_from, go_till, step_over_by, in_column, matrix, arr):
    for i in range(start_from, go_till, step_over_by):
        arr.append(matrix[i][in_column])
        matrix[i].pop(in_column)


def spiralOrder(matrix):
    arr = []
    while True:
        go_left_to_right(start_from=0, go_till=len(matrix[0]),
                         step_over_by=1, in_row=0, matrix=matrix, arr=arr)

        matrix.pop(0)
        if (len(matrix) == 0 or len(matrix[0]) == 0):
            break

        go_top_to_down(start_from=0, go_till=len(matrix),
                       step_over_by=1, in_column=len(matrix[0])-1, matrix=matrix, arr=arr)
        if (len(matrix) == 0 or len(matrix[0]) == 0):
            break

        right_to_left(start_from=len(matrix[0])-1, go_till=-1,
                      step_over_by=-1, in_row=len(matrix)-1, matrix=matrix, arr=arr)

        matrix.pop(len(matrix)-1)

        if (len(matrix) == 0 or len(matrix[0]) == 0):
            break
        down_to_top(len(matrix)-1, go_till=-1, step_over_by=-
                    1, in_column=0, matrix=matrix, arr=arr)

        if (len(matrix) == 0 or len(matrix[0]) == 0):
            break

    return arr


# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12]]
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[7], [9], [6]]
print(spiralOrder(matrix=matrix))
# spiralOrder(matrix=matrix)
