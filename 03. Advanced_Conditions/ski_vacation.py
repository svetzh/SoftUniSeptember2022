days_stay = int(input())
type_room = input()
rate = input()

price_room = 0

if type_room == "room for one person":
    price_room = 18.00
    if days_stay < 10:
        price_room = price_room * (days_stay - 1)
    elif 10 < days_stay < 15:
        price_room = price_room * (days_stay - 1)
    elif days_stay > 15:
        price_room = price_room * (days_stay - 1)
elif type_room == "apartment":
    price_room = 25.00
    if days_stay < 10:
        price_room = price_room * (days_stay - 1) * .7
    elif 10 < days_stay < 15:
        price_room = price_room * (days_stay - 1) * .65
    elif days_stay > 15:
        price_room = price_room * (days_stay - 1) * .5
elif type_room == "president apartment":
    price_room = 35.00
    if days_stay < 10:
        price_room = price_room * (days_stay - 1) * .9
    elif 10 < days_stay < 15:
        price_room = price_room * (days_stay - 1) * .85
    elif days_stay > 15:
        price_room = price_room * (days_stay - 1) * .80

if rate == "positive":
    price_room = price_room * 1.25
elif rate == "negative":
    price_room = price_room * .9

print(f"{price_room:.2f}")