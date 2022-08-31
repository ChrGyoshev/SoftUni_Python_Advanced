from collections import deque
expression = input().split()

digits = deque()

for symbol in expression:
    if symbol in "*+-/":
        while len(digits) > 1:
            first_digit = digits.popleft()
            second_digit = digits.popleft()
            result = 0
            if symbol == "*":
                result = first_digit * second_digit
            elif symbol == "/":
                result = first_digit // second_digit
            elif symbol == "+":
                result = first_digit + second_digit
            else:
                result = first_digit - second_digit
            digits.appendleft(result)
    else:
        digits.append(int(symbol))

print (digits.popleft())
