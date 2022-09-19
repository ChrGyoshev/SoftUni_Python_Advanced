def age_assignment(*args,**kwargs):
    result = {}
    final_result = ''
    for k,v in kwargs.items():
        for name in args:
            if name[0] == k:
                result[name] = v
    sorting_result = sorted(result.items(),key= lambda  kvpt: kvpt[0])

    for data in sorting_result:
        final_result += f"{data[0]} is {data[1]} years old.\n"

    return final_result





