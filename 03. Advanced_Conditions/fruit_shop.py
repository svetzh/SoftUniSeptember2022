from sys import exit

fruit_product = input()
day_of_week = input()
quantity = float(input())
price = 0

if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" or \
        day_of_week == "Friday":
    if fruit_product == "banana":
        price = 2.5
    elif fruit_product == "apple":
        price = 1.2
    elif fruit_product == "orange":
        price = .85
    elif fruit_product == "grapefruit":
        price = 1.45
    elif fruit_product == "kiwi":
        price = 2.7
    elif fruit_product == "pineapple":
        price = 5.5
    elif fruit_product == "grapes":
        price = 3.85
    else:
        print("error")
        exit()
elif day_of_week == "Saturday" or day_of_week == "Sunday":
    if fruit_product == "banana":
        price = 2.7
    elif fruit_product == "apple":
        price = 1.25
    elif fruit_product == "orange":
        price = .9
    elif fruit_product == "grapefruit":
        price = 1.6
    elif fruit_product == "kiwi":
        price = 3
    elif fruit_product == "pineapple":
        price = 5.6
    elif fruit_product == "grapes":
        price = 4.2
    else:
        print("error")
        exit()

price_per_fruit = quantity * price

print(f"{price_per_fruit:.2f}")
