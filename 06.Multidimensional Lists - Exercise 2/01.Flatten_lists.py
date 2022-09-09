lists = input().split("|")
matrix = []
for ele in lists:
    current = ele.split()
    matrix.append(current)
matrix.reverse()
result = ""
for ele in matrix:
    for x in ele:
        result += x + " "

print(result)