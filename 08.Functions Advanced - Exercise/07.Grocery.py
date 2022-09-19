def grocery_store(**kwargs):
    result = ""
    sorted_grocery = sorted(kwargs.items(), key= lambda kvpt: (-(kvpt[1]), (-len(kvpt[0]),kvpt[0])))
    for key,value in sorted_grocery:
        result += (f'{key}: {value}') + "\n"
    return result














