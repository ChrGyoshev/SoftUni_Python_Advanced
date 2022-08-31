#create two unique sets
first_nums = set(int(x) for x in input().split())
second_nums = set(int(x) for x in input().split())

#n itterations
n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == "Add":
        if command[1] == "First":
            [first_nums.add(int(x)) for x in command[2:]]
        else:
            [second_nums.add(int(x)) for x in command[2:]]

    elif command[0] == "Remove":
        if command[1] == "First":
            first_nums = first_nums.difference([int(x) for x in command[2:]])
        else:
            second_nums = second_nums.difference([int(x) for x in command[2:]])

    elif command[0] == "Check" and command[1] == "Subset":
       print(first_nums.issubset(second_nums) or second_nums.issubset(first_nums))
print(*sorted(first_nums),sep= ", ")
print(*sorted(second_nums),sep = ", ")