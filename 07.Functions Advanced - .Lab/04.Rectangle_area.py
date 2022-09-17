def rectangle(len,width):
    def area():
        return len * width

    def perimeter():
        return (len+width)*2

    if not isinstance(len,int) or not isinstance(width,int):
        return "Enter valid values!"

    return f'''Rectangle area: {area()}
Rectangle perimeter: {perimeter()}'''










