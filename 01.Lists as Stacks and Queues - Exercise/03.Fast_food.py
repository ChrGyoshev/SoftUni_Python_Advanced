from collections import deque
quantity_of_food = int(input())
quantity_of_order = deque(list(map(int,input().split())))

print(max(quantity_of_order))

while quantity_of_order:
    if quantity_of_food >= quantity_of_order[0]:
        quantity_of_food -= quantity_of_order[0]
        quantity_of_order.popleft()
    else:
        print(f'Orders left:',end=" ")
        print(*quantity_of_order)
        break
if not quantity_of_order:
    print("Orders complete")



