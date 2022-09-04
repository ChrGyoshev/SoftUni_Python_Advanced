n = int(input())
matrix = []

for _ in range(n):
    columns = [int(x) for x in input().split()]
    matrix.append(columns)
print(sum(matrix[i][i] for i in range(n)))
