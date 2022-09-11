def move_left(row, col):
    return row, col-1

def move_right(row,col):
    return row, col+1

def move_up(row,col):
    return row-1,col

def move_down(row,col):
    return row+1, col

n = int(input())
matrix = []
bags_of_tea = 0
for row in range(n):
    row_elements = input().split()
    matrix.append(row_elements)

    for col in range(n):
        if matrix[row][col] == "A":
            alice_row = row
            alice_col = col
            matrix[row][col] = "*"



while True:
    if bags_of_tea >= 10:
        break
    command = input()
    if command == "up":
        alice_row,alice_col = move_up(alice_row,alice_col)

    elif command == "down":
        alice_row,alice_col = move_down(alice_row,alice_col)
    elif command == "left":
        alice_row,alice_col = move_left(alice_row,alice_col)
    elif command == "right":
        alice_row,alice_col = move_right(alice_row,alice_col)



    if alice_row <0 or alice_col <0 or alice_row >= n or alice_col >= n:
        break


    if matrix[alice_row][alice_col] == "R":
        matrix[alice_row][alice_col] = "*"
        break
    if matrix[alice_row][alice_col].isdigit():
        bags_of_tea += int(matrix[alice_row][alice_col])
        matrix[alice_row][alice_col]="*"

    else:
        matrix[alice_row][alice_col] = "*"



if bags_of_tea >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for data in matrix:
    print(*data)