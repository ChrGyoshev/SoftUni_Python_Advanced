
first_player, second_player = input().split(", ")
matrix = []
for row in range(6):
    matrix.append([x for x in input().split()])

player_one_need_rest = False
player_two_need_rest = False

while True:


#first_player_move
    first_player_coord = input()
    if not player_one_need_rest:
        rows,cols =map(int,first_player_coord.strip("(").strip(")").split(", "))
        if matrix[rows][cols] =="E":
            print(f"{first_player} found the Exit and wins the game!" )
            break
        elif matrix[rows][cols] == "T":
            print(f"{first_player} is out of the game! The winner is {second_player}." )
            break
        elif matrix[rows][cols] == "W":
            print(f"{first_player} hits a wall and needs to rest.")
            player_one_need_rest = True
    else:
        player_one_need_rest = False

#second_player_move
    second_player_coord = input()
    if not player_two_need_rest:
        rows, cols = map(int, second_player_coord.strip("(").strip(")").split(", "))
        if matrix[rows][cols] =="E":
            print(f"{second_player} found the Exit and wins the game!")
            break
        elif matrix[rows][cols] == "T":
            print(f"{second_player} is out of the game! The winner is {first_player}.")
            break
        elif matrix[rows][cols] == "W":
            print(f"{second_player} hits a wall and needs to rest.")
            player_two_need_rest = True
    else:
        player_two_need_rest = False


