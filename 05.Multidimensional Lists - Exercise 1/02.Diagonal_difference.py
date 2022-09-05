n = int(input())
matrix = []
primary = 0
secondary = 0
for row in range(n):
    matrix.append([int(x) for x in input().split()])
    primary += matrix[row][row]
    secondary += matrix[row][n-1-row]
print(abs(primary - secondary))






