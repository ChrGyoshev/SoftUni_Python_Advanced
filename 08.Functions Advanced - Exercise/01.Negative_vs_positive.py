def calculate(data):
    positives =0
    negatives = 0
    for num in data:
        if num > 0:
            positives += num
        else:
            negatives += num
    print(negatives)
    print(positives)
    if abs(negatives) > positives:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")

data = calculate([int(x) for x in input().split()])
