from collections import deque
kids_names = deque(input().split())
tosses = int(input())

while len(kids_names) >1:
    result = kids_names.rotate(-tosses)
    print(f'Removed {kids_names.pop()}')

print(f'Last is {kids_names.pop()}')