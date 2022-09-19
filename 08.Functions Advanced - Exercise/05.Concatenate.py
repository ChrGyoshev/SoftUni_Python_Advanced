def concatenate(*args,**kwargs):
    result = ''
    for str in args:
        result+= str

    for key,value in kwargs.items():
        if key in result:
            result = result.replace(key,value)
    return result