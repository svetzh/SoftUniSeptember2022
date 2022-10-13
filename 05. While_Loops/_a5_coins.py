change = float(input())
coins = 0

while change > 0:
    if change >= 2:
        change -= 2
    elif change >= 1:
        change -= 1
    elif change >= .5:
        change -= .5
    elif change >= .2:
        change -= .2
    elif change >= .1:
        change -= .1
    elif change >= .05:
        change -= .05
    elif change >= .02:
        change -= .02
    elif change >= .01:
        change -= .01
    change = round(change, 2)
    coins += 1

print(coins)
