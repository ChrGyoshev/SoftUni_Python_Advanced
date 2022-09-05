
rows = int(input())
matrix =[]
for row in range(rows):
    elements = [(int(x)) for x in input().split(", ")]
    matrix.append(elements)
print(sum(matrix,[]))
