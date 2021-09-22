def change (amount):
    if amount == 24:
        return [5,5,7,7]
    if amount == 25:
        return [5,5,5,5,5]
    if amount == 26:
        return [7,7,7,5]
    if amount == 27:
        return [5,5,5,5,7]
    coin = change(amount - 5)
    coin.append(5)
    return coin

 