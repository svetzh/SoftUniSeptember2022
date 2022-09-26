budget = int(input())
season = input()
num_fishermen = int(input())

price_boat = 0

if season == "Spring":
    price_boat = 3000
elif season == "Summer" or season == "Autumn":
    price_boat = 4200
elif season == "Winter":
    price_boat = 2600

if num_fishermen <= 6:
    price_boat -= price_boat * .1
elif 6 < num_fishermen < 12:
    price_boat -= price_boat * .15
elif num_fishermen >= 12:
    price_boat -= price_boat * .25

if num_fishermen % 2 == 0 and season != "Autumn":
    price_boat -= price_boat * 0.05

money_left = abs(budget - price_boat)

if budget >= price_boat:
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    print(f"Not enough money! You need {money_left:.2f} leva.")
