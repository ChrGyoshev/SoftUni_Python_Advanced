def get_next_position(direct, row, col):
    if direct == "up":
        return row - 1, col
    elif direct == "down":
        return row + 1, col
    elif direct == "left":
        return row, col - 1
    elif direct == "right":
        return row, col + 1


presents = int(input())
n = int(input())
matrix = []

total_good_kids = 0
delivered_presents_to_good_kids = 0
santa_row = 0
santa_col = 0

for row in range(n):
    row_elements = input().split()
    matrix.append(row_elements)

    for col in range(n):
        if row_elements[col] == "V":
            total_good_kids += 1
        elif row_elements[col] == "S":
            santa_row = row
            santa_col = col

while True:
    line = input()
    if line == "Christmas morning":
        break
    matrix[santa_row][santa_col] = "-"
    santa_row,santa_col = get_next_position(line,santa_row,santa_col)

    if matrix[santa_row][santa_col] == "V":
        presents -=1
        delivered_presents_to_good_kids +=1
    elif matrix[santa_row][santa_col] == "C":
        #left
        if matrix[santa_row][santa_col-1] == "V" and presents:
            delivered_presents_to_good_kids+=1
            presents-=1
            matrix[santa_row][santa_col-1] = "-"
        elif matrix[santa_row][santa_col-1] == "X" and presents:
            presents -= 1
            matrix[santa_row][santa_col-1] = "-"
        #right
        if matrix[santa_row][santa_col+1] == "V" and presents:
            delivered_presents_to_good_kids +=1
            presents -=1
            matrix[santa_row][santa_col+1] = "-"
        elif matrix[santa_row][santa_col+1] == "X"and presents:
            presents -=1
            matrix[santa_row][santa_col+1] = "-"
        #up
        if matrix[santa_row-1][santa_col] == "V"and presents:
            delivered_presents_to_good_kids +=1
            presents -=1
            matrix[santa_row-1][santa_col] = "-"
        elif matrix[santa_row-1][santa_col] == "X"and presents:
            presents -=1
            matrix[santa_row-1][santa_col] = "-"
        #down
        if matrix[santa_row+1][santa_col] == "V"and presents:
            delivered_presents_to_good_kids+=1
            presents -=1
            matrix[santa_row+1][santa_col] = "-"
        elif matrix[santa_row+1][santa_col] == "X"and presents:
            presents -=1
            matrix[santa_row+1][santa_col] = "-"

    matrix[santa_row][santa_col] = "S"
    if presents == 0 or delivered_presents_to_good_kids == total_good_kids:
        break
if presents ==0 and delivered_presents_to_good_kids < total_good_kids:
    print("Santa ran out of presents!")

for row in matrix:
    print(*row,sep=" ")
if delivered_presents_to_good_kids == total_good_kids:
    print(f'Good job, Santa! {total_good_kids} happy nice kid/s.')
else:
    print(f"No presents for {total_good_kids - delivered_presents_to_good_kids} nice kid/s.")

