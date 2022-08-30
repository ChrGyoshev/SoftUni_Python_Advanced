n = int(input())
odd_numbers = set()
even_numbers = set()
sum_even = 0
sum_odd = 0
for row in range (1, n+1):
    name = (sum(ord(x) for x in input()) // row)
    if name % 2 == 0:
        even_numbers.add(name)
        sum_even += name
    else:
        odd_numbers.add(name)
        sum_odd += name
if sum_even == sum_odd:
    result = odd_numbers.union(even_numbers)
elif sum_even > sum_odd:
    result = odd_numbers.symmetric_difference(even_numbers)
else:
    result = odd_numbers.difference(even_numbers)
#print(", ".join(str(el) for el in result))
print(*result, sep=", ")


