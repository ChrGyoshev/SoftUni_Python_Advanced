def sorting_cheeses(**kwargs):
    sorting_cheeses = sorted(kwargs.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))
    result = ''
    for name, quantities in sorting_cheeses:
        sorted_quantities =sorted(quantities, reverse=True)
        result += name + "\n"
        result += "\n".join([str(x) for x in sorted_quantities]) + "\n"

    return result
