text = input()
data_list = []

for index in range(len(text)):
    if text[index] == "(":
        data_list.append(index)
    elif text[index] == ")":
        print(text[data_list.pop():index+1])