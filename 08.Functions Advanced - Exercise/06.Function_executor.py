def func_executor(*args):
    result = ""
    for func, nums in args:
        function = func(*nums)
        result += f"{func.__name__} - {function}" + "\n"
    return result









