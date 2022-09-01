from collections import deque
working_bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
honey_process = deque(input().split())
total_honey_made = 0

while working_bees and nectar:
    current_bee = working_bees[0]
    current_nectar = nectar.pop()
    if current_nectar >= current_bee:
        working_bees.popleft()
        current_symbol = honey_process.popleft()
        if current_symbol == "+":
            total_honey_made += abs(current_bee + current_nectar)
        elif current_symbol == "-":
            total_honey_made += abs(current_bee - current_nectar)
        elif current_symbol == "*":
            total_honey_made += abs(current_bee * current_nectar)
        elif current_symbol =="/" and current_nectar > 0:
            total_honey_made += abs(current_bee / current_nectar)


print(f"Total honey made: {total_honey_made}")
if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")