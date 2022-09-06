import sys

rows,columns = [int(x) for x in input().split()]
matrix = []
max_submatrix = []
min = -sys.maxsize
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for row in range(rows-2):
    for col in range(columns - 2):
        sub_matrix = [matrix[row][col], matrix[row][col+1],matrix[row][col+2],matrix[row+1][col],
                      matrix[row+1][col+1],matrix[row+1][col+2],matrix[row+2][col],matrix[row+2][col+1],matrix[row+2][col+2]]
        if sum(sub_matrix) > min:
            min = sum(sub_matrix)
            max_submatrix= sub_matrix

print(f"Sum = {min}")
print(" ".join([str(max_submatrix[x])for x in range(3)]))
print(" ".join([str(max_submatrix[x])for x in range(3,6)]))
print(" ".join([str(max_submatrix[x])for x in range(6,9)]))