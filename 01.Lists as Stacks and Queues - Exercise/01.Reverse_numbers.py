string = [int(el) for el in input().split()]
while string:
    if len(string)>1:
        print(string.pop(),end=" ")
    else:
        print(string.pop())