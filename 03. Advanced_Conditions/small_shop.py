product = input()
city = input()
quantity = float(input())
price = 0

if city == "Sofia":
    if product == "coffee":
        price = .5
        price *= quantity
    elif product == "water":
        price = .8
        price *= quantity
    elif product == "beer":
        price = 1.2
        price *= quantity
    elif product == "sweets":
        price = 1.45
        price *= quantity
    elif product == "peanuts":
        price = 1.60
        price *= quantity
elif city == "Plovdiv":
    if product == "coffee":
        price = .4
        price *= quantity
    elif product == "water":
        price = .7
        price *= quantity
    elif product == "beer":
        price = 1.15
        price *= quantity
    elif product == "sweets":
        price = 1.30
        price *= quantity
    elif product == "peanuts":
        price = 1.50
        price *= quantity
elif city == "Varna":
    if product == "coffee":
        price = .45
        price *= quantity
    elif product == "water":
        price = .7
        price *= quantity
    elif product == "beer":
        price = 1.1
        price *= quantity
    elif product == "sweets":
        price = 1.35
        price *= quantity
    elif product == "peanuts":
        price = 1.55
        price *= quantity
print(round((price),4))