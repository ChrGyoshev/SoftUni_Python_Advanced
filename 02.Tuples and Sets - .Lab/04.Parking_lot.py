num_commands = int(input())
parking_lot = set()
for _ in range(num_commands):
    command,plate = input().split(", ")
    if command == "IN":
        parking_lot.add(plate)
    elif command == "OUT":
        parking_lot.remove(plate)
if not parking_lot:
    print('Parking Lot is Empty')
else:
    print("\n".join(parking_lot))
