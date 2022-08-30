data = input()
dictonary = {}
for chr in data:
    if not chr in dictonary:
        dictonary[chr] = 0
    dictonary[chr] +=1
print("\n".join(sorted(f'{k}: {v} time/s'for k,v in dictonary.items())))