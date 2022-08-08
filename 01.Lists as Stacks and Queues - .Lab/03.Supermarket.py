from collections import deque
string = input()
line = deque()

while not string == "End":
    if string == "Paid":
        while line:
            print(line.popleft())
    else:
        line.append(string)
    string = input()
print(f'{len(line)} people remaining.')