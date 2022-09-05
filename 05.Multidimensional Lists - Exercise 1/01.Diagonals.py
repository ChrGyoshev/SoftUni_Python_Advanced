n = int(input())
matrix = []


for _ in range(n):
    matrix.append([int(el) for el in input().split(", ")])
#left_diagonal
sum_left  = 0
left = []
for rows in range(n):
    sum_left += matrix[rows][rows]
    left.append(matrix[rows][rows])

#right_diagonal
sum_right= 0
right = []

k=n -1
for i in range(n):
    sum_right += matrix[i][k]
    right.append(matrix[i][k])
    k-=1
print(f"Primary diagonal: {', '.join(str(x)for x in left)}. Sum: {sum_left}")
print(f"Secondary diagonal: {', '.join(str(x)for x in right)}. Sum: {sum_right}")



