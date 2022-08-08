n = int(input())
stack = []

for _ in range (n):
    command = input().split()
    current_command = int(command[0])
    if current_command == 1:
        stack.append(int(command[1]))
    elif current_command == 2:
        if stack:
            stack.pop()
    elif current_command == 3:
        if stack:
            print(max(stack))
    elif current_command == 4:
        if stack:
            print(min(stack))

while stack:
    if len(stack) > 1:
        print(stack.pop(),end= ", ")
    else:
        print(stack.pop())

