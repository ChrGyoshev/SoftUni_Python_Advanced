expression = input()
data = []
balanced = True
for ch in expression:
    if ch in "([{":
        data.append(ch)
    elif not data:
        balanced=False
        break
    else:
        last_opening = data.pop()
        if f'{last_opening}{ch}' not in "(){}[]":
            balanced = False
            break
if balanced:
    print("YES")
else:
    print("NO")