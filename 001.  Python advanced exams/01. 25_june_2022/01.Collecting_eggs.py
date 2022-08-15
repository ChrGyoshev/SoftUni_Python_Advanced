from collections import deque
eggs_size = deque(list(map(int,input().split(", "))))
piece_of_paper = list(map(int,input().split(", ")))
boxes = 0
while eggs_size:
    if not piece_of_paper:
        break
    current_egg = eggs_size.popleft()
    if current_egg <= 0:
        continue
    elif current_egg == 13:
        piece_of_paper[0], piece_of_paper[-1] = piece_of_paper[-1],piece_of_paper[0]

    elif current_egg + piece_of_paper[-1] > 50:
        piece_of_paper.pop()
        continue
    else:
        boxes += 1
        piece_of_paper.pop()
if boxes >0:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs_size:
    print("Eggs left: ",end ='')
    print(", ".join([str(el) for el in eggs_size]))
if piece_of_paper:
    print("Pieces of paper left: ",end='')
    print(", ".join([str(el) for el in piece_of_paper]))
