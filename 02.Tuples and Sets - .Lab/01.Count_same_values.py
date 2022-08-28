numbers = (float(el) for el in input().split())
occ = {}
for num in numbers:
    if num not in occ:
        occ[num] = 0
    occ[num]+=1
print("\n".join([f"{k} - {v} times"for k,v in occ.items()]))
