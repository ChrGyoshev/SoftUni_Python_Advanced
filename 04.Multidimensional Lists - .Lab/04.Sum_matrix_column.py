
rows,columns = [int(x) for x in input().split(", ")]
matrix= []
for _ in range(rows):
    nums=([int(x) for x in input().split()])
    matrix.append(nums)

for col_index in range(columns):
    res =0
    for row_index in range(rows):
        res+=matrix[row_index][col_index]
    print(res)






