def even_odd (*args):
    command = args[-1]
    if command == "even":
        return [int(x) for x in args[:-1] if x % 2 ==0]
    else:
        return [int(x) for x in args[:-1] if x%2 != 0]


