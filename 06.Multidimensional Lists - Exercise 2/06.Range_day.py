def get_next_pos(direct, row, col, step):
    if direct == "left":
        return row, col - step
    elif direct == "right":
        return row, col + step
    elif direct == "up":
        return row - step, col
    elif direct == "down":
        return row + step, col

def is_inside(row,col,size):
    return  0 <= row < size and 0 <= col < size

size = 5
matrix = []
targets = 0
targets_coords = []
position_row = 0
position_col = 0

for row in range(size):
    data = input().split()
    matrix.append(data)

    for col in range(size):
        if data[col] == "A":
            position_row = row
            position_col = col
        elif data[col] == "x":
            targets += 1

commands = int(input())
targets_left = targets

for _ in range(commands):
    current_command = input().split()
    direction = current_command[1]
    if current_command[0] == "move":
        step = int(current_command[2])

        #getting next position
        next_row, next_col = get_next_pos(direction, position_row, position_col, step)
        #check boundary
        if is_inside(next_row,next_col,size) and matrix[next_row][next_col] == ".":
            matrix[position_row][position_col] = "."
            matrix[next_row][next_col] = "A"
            position_row,position_col = next_row, next_col
    else:
        bullet_row,bullet_col = position_row,position_col
        while True:
            bullet_row,bullet_col = get_next_pos(direction,bullet_row,bullet_col,1)
            if is_inside(bullet_row,bullet_col,size):
                if matrix[bullet_row][bullet_col] == "x":
                    targets_left -=1
                    targets_coords.append([bullet_row,bullet_col])
                    matrix[bullet_row][bullet_col] = "."
                    break
            else:
                break
        if targets_left == 0:
            break

if targets_left == 0:
    print(f"Training completed! All {targets} targets hit.")
else:
    print(f"Training not completed! {targets_left} targets left.")
for data in targets_coords:
    print(data)








