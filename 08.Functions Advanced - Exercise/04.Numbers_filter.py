def even_odd_filter(**kwargs):
    result = {}
    for command,list in kwargs.items():
        if command == "odd":
            list = [int(x) for x in list if x % 2 != 0]
            result[command] = list
        elif command == "even":
            list = [int(x) for x in list if x % 2 ==0]
            result[command] = list
    sorting = sorted(result.items(), key = lambda x: (-len(x[1])))
    converted = dict(sorting)
    return converted





