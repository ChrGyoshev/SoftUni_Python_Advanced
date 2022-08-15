from collections import deque
num_of_petrol_pumps = int(input())
pumps = deque()
for _ in range(num_of_petrol_pumps):
    petrol,distance = input().split()
    petrol = int(petrol)
    distance = int(distance)
    pumps.append([petrol,distance])

for i in range(num_of_petrol_pumps):
    tank = 0
    failed = False
    for fuel,distance in pumps:
        tank += fuel

        if distance > tank:
            failed = True
            break
        else:
            tank -= distance
    if failed:
        pumps.rotate(num_of_petrol_pumps-1)
    else:
        print(i)
        break

