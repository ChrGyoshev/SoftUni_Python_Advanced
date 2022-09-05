rows, col = [int(x) for x in input().split(", ")]
matrix = []
max_sum = -9999999999999999999999
max_sum_matrix = []
for _ in range(rows):
    matrix.append([int(el) for el in input().split(", ")])
for row_i in range(rows-1):
    for col_i in range(col-1):
        sub_matrix = [matrix[row_i][col_i], matrix[row_i][col_i+1],
                      matrix[row_i+1][col_i],matrix[row_i+1][col_i+1]]

        current_sum = sum(sub_matrix)
        if current_sum > max_sum:
            max_sum = current_sum
            max_sum_matrix = sub_matrix.copy()
print(max_sum_matrix[0],max_sum_matrix[1])
print(max_sum_matrix[2],max_sum_matrix[3])
print(max_sum)
