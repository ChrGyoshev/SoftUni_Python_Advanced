n = int(input())
matrix = []

for _ in range(n):
    matrix.append(list(input()))
searched = input()


for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        is_found = False
        if searched == matrix[row][col]:
            result = (row,col)
            print(result)
            is_found=True
            break
    if is_found:
        break
if not is_found:
    print(f"{searched} does not occur in the matrix")




