clothes_in_the_box = list(map(int,input().split()))
rack_capacity = int(input())
racks = 1
current_rack = rack_capacity
while clothes_in_the_box:
    if clothes_in_the_box[-1] <= current_rack:
        current_rack -= clothes_in_the_box.pop()
    else:
        racks +=1
        current_rack = rack_capacity
print(racks)