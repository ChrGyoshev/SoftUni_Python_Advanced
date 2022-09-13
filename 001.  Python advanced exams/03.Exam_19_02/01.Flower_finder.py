from collections import deque
words = ['rose','tulip','lotus','daffodil']
vowels = deque(input().split())
consonants = input().split()
result = words.copy()
is_found = False

while vowels and consonants:
    current_vowel = vowels.popleft()
    curr_consonant = consonants.pop()
    for obj in range(len(words)):
        if current_vowel in result[obj]:
            result[obj] = result[obj].replace(current_vowel, "")
        if curr_consonant in result[obj]:
            result[obj] = result[obj].replace(curr_consonant, "")
        if "" in result:
            is_found = True
            break
    if is_found:
        break





if is_found:
    word_index = result.index("")
    print(f"Word found: {words[word_index]}")
if not is_found:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)} ")
if consonants:
    print(f"Consonants left: {' '.join(consonants)} ")



