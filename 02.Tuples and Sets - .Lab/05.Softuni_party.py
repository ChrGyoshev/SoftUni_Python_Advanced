num_of_guest = int(input())
guests = set()

for _ in range(num_of_guest):
    guest = input()
    guests.add(guest)

command = input()
while not command == "END":
    guests.remove(command)
    command = input()

print(len(guests))
print("\n".join(sorted(guests)))

