n,m = [ int(el) for el in input().split()]
first_elements = set()
second_elements = set()
for _ in range(n):
    element = first_elements.add(input())

for _ in range(m):
    element = second_elements.add(input())
print("\n".join(first_elements.intersection(second_elements)))