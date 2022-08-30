n = int(input())
data = set()
for _ in range(n):
    data = data.union(input().split())
print("\n".join(el for el in data))
