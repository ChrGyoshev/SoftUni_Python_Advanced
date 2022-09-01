from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])
toys_collection = {
    150: "Doll",
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}
crafted_presents = {}
while materials and magic_level:
    current_material = materials.pop()
    current_magic = magic_level.popleft()
    multi = current_material * current_magic
    if multi in toys_collection:
        toy = toys_collection[multi]
        if toy in crafted_presents:
            crafted_presents[toy] += 1
        else:
            crafted_presents[toy] = 1
    elif multi < 0:
        materials.append(current_material + current_magic)
    elif multi > 0:
        materials.append(current_material + 15)
    else:
        if current_material == 0 and current_magic == 0:
            continue
        elif current_material == 0:
            magic_level.appendleft(current_magic)
        else:
            materials.append(current_material)
if "Bicycle" in crafted_presents and "Teddy bear" in crafted_presents  or \
        "Doll" in crafted_presents and "Wooden train" in crafted_presents:
        print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(reversed([str(x)for x in materials]))}")

if magic_level:
    print(f"Magic left: {', '.join([str(x) for x in magic_level])}")

for present, count in sorted(crafted_presents.items()):
    print(f"{present}: {count}")

