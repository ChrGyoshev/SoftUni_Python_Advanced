from collections import deque
bows = list(map(int,input().split(", ")))
customers = deque(list(map(int,input().split(", "))))

while customers:
    if not bows:
        break
    current_bow = bows[-1]
    current_customer = customers[0]
    if current_customer == current_bow:
        bows.pop()
        customers.popleft()
    elif current_bow > current_customer:
        bows[-1] = bows[-1] - customers.popleft()
    elif current_bow < current_customer:
        customers[0] = customers[0] - bows.pop()
if not customers:
    print("Great job! You served all the customers.")
    if bows:
        print(f'Bowls of ramen left: {", ".join([str(el) for el in bows])}')
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f'Customers left: {", ".join([str(el) for el in customers])}')
