def get_next_direction(direct, row, col):
    if direct == "up":
        row, col = row - 1, col
        if row < 0:
            row = size - 1
        return row, col

    elif direct == "down":
        row, col = row + 1, col
        if row >= size:
            row = 0
        return row, col

    elif direct == "left":
        row, col = row, col - 1
        if col < 0:
            col = size - 1
        return row, col

    elif direct == "right":
        row, col = row, col + 1
        if col >= size:
            col = 0
        return row, col


size = 6
matrix = []

water_deposit = False
concrete_deposite = False
metal_deposite = False

rover_row = 0
rover_col = 0

for row in range(size):
    row_data = input().split()
    matrix.append(row_data)

    for col in range(size):
        if row_data[col] == "E":
            rover_row = row
            rover_col = col

command = input().split(", ")

for current in range(len(command)):
    direction = command[current]
    next_row, next_col = get_next_direction(direction, rover_row, rover_col)
    matrix[rover_row][rover_col] = "-"
    #rover new location
    rover_row, rover_col = next_row, next_col

#water_deposit
    if matrix[rover_row][rover_col] == "W":
        print(f"Water deposit found at ({rover_row}, {rover_col})")
        water_deposit = True
        matrix[rover_row][rover_col] = "E"

# metal_deposite
    elif matrix[rover_row][rover_col] == "M":
        print(f'Metal deposit found at ({rover_row}, {rover_col})')
        metal_deposite = True
        matrix[rover_row][rover_col] = "E"

#concrete_deposite
    elif matrix[rover_row][rover_col] == "C":
        print(f"Concrete deposit found at ({rover_row}, {rover_col})")
        concrete_deposite = True
        matrix[rover_row][rover_col] = "E"

#Rock
    elif matrix[rover_row][rover_col] == "R":
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        break

if water_deposit and concrete_deposite and metal_deposite:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")


