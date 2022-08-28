num_of_students = int(input())
students = {}
for _ in range(num_of_students):
    name,grade = input().split()
    grade = float(grade)
    if name not in students:
        students[name] = []
    students[name].append(grade)

for k,v in students.items():
    print(f"{k} -> {' '.join([f'{el:.2f}'for el in v])} "
          f"(avg: {sum(v)/len(v):.2f})")