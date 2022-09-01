from collections import deque

chocolate = [int(x) for x in input().split(", ")]
milk = deque([int(x) for x in input().split(", ")])
milkshakes = 0
while chocolate and milk and milkshakes<5:
    current_chocolate = chocolate[-1]
    current_milk = milk[0]
    if current_chocolate <=0 and current_milk <= 0 :
        chocolate.pop()
        milk.popleft()
        continue
    if current_chocolate<=0:
        chocolate.pop()
        continue
    if current_milk <=0:
        milk.popleft()
        continue

    if current_chocolate == current_milk:
        milkshakes +=1
        chocolate.pop()
        milk.popleft()
    else:
        milk.popleft()
        milk.append(current_milk)
        chocolate[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolate:
    print(f'Chocolate: {", ".join(str(el) for el in chocolate)}')
else:
    print("Chocolate: empty")
if milk:
    print(f'Milk: {", ".join(str(x) for x in milk)}')
else:
    print("Milk: empty")