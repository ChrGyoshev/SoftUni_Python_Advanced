rows,cols = [int(x) for x in input().split()]
matrix = []

for i in range(rows):
    matrix.append(input().split())
result = 0
for row in range(rows-1):

    for col in range(cols-1):
        sub_matrix = [matrix[row][col],matrix[row][col+1],matrix[row+1][col],matrix[row+1][col+1]]
        if sub_matrix[0] == sub_matrix[1] and sub_matrix[0] == sub_matrix[2] and sub_matrix[0] == sub_matrix[3]:
            result+=1
print(result)







