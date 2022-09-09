def is_valid(first,second,matrix):
    if 0<= first < len(matrix) and 0<= second < len(matrix):
        return  True
    else:
        print("Invalid coordinates")


n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split()])

while True:
    command = input().split()
    if command[0] == "END":
        break
    checker = is_valid(int(command[1]),int(command[2]),matrix)
    if checker:
        if command[0] == "Add":
            matrix[int(command[1])][int(command[2])] += int(command[3])
        elif command[0] == "Subtract":
            matrix[int(command[1])][int(command[2])] -= int(command[3])

for obj in matrix:
    print(" ".join([str(x)for x in obj]))