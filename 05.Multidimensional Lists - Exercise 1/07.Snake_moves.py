rows,cols = [int(x) for x in input().split()]
command = input()
idx = 0
matrix = []

for row in range(rows):
    row_elements = []
    for col in range(cols):
        row_elements.append(command[idx % len(command)])
        idx +=1

    if row % 2 == 0:
        print(*row_elements, sep= "")
    else:
        print(*reversed(row_elements),sep = "")



