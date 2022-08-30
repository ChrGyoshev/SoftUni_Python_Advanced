def calc(range_info):
    start,end = [int(x) for x in range_info.split(",")]
    return set(range(start,end+1))
n = int(input())
max_intersection = set()

for _ in range(n):
    line = input().split("-")
    first_set = calc(line[0])
    second_set = calc(line[1])
    current_intersection = first_set.intersection(second_set)

    if len(current_intersection) > len(max_intersection):
        max_intersection = current_intersection
print(f"Longest intersection is {list(max_intersection)} with length {len(max_intersection)}")
