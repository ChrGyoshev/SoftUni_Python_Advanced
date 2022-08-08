from collections import deque
quantity_of_water = int(input())
command = input()
people_in_queue = deque()
while not command == "Start":
    people_in_queue.append(command)
    command = input()

command = input()
while not command == "End":
    command = command.split()
    if command[0].isdigit():
        if int(command[0]) <= quantity_of_water:
            print(f"{people_in_queue.popleft()} got water" )
            quantity_of_water -= int(command[0])
        else:
            print(f"{people_in_queue.popleft()} must wait" )
    else:
        quantity_of_water += int(command[1])
    command = input()

print(f"{quantity_of_water} liters left")
