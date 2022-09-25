type_flowers = input()
number_of_flowers = int(input())
budget = int(input())

roses_price = 5
dahlias_price = 3.8
tulips_price = 2.8
narcissus_price = 3
gladiolus_price = 2.5

price = 0

if type_flowers == "Roses":
    price = roses_price * number_of_flowers
    if number_of_flowers > 80:
        price -= price * .1
    else:
        price
elif type_flowers == "Dahlias":
    price = dahlias_price * number_of_flowers
    if number_of_flowers > 90:
        price -= price * .15
    else:
        price
elif type_flowers == "Tulips":
    price = tulips_price * number_of_flowers
    if number_of_flowers > 80:
        price -= price * .15
    else:
        price
elif type_flowers == "Narcissus":
    price = narcissus_price * number_of_flowers
    if number_of_flowers < 120:
        price += price * .15
    else:
        price
elif type_flowers == "Gladiolus":
    price = gladiolus_price * number_of_flowers
    if number_of_flowers < 80:
        price += price * .2
    else:
        price

diff = abs(budget - price)

if budget >= price:
    print(f"Hey, you have a great garden with {number_of_flowers} {type_flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
