def count(b):
    color = []
    amount = []
    for i in b:
        if i != "_":
            if i not in color:
                color.append(i)
                amount.append(1)
            else:
                amount[color.index(1)]+=1
    return amount
                