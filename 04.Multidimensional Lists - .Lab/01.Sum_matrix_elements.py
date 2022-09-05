rows,columns = [int(x) for x in input().split(", ")]
matrix = []
for _ in range(rows):
    elements = [int(x) for x in input().split(", ")]
    matrix.append(elements)
print(sum(([sum(x) for x in matrix])))
print(matrix)