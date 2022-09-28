month = input()
number_nights = int(input())

studio_entire_stay = 0
apartment_entire_stay = 0

if month == "May" or month == "October":
    studio_entire_stay = number_nights * 50
    apartment_entire_stay = number_nights * 65
    if 7 < number_nights < 14:
        studio_entire_stay -= studio_entire_stay * .05
    elif number_nights > 14:
        studio_entire_stay -= studio_entire_stay * .3
        apartment_entire_stay -= apartment_entire_stay * .1
elif month == "June" or month == "September ":
    studio_entire_stay = number_nights * 75.2
    apartment_entire_stay = number_nights * 68.7
    if number_nights > 14:
        studio_entire_stay -= studio_entire_stay * .2
        apartment_entire_stay -= apartment_entire_stay * .1
elif month == "July" or month == "August":
    studio_entire_stay = number_nights * 76
    apartment_entire_stay = number_nights * 77
    if number_nights > 14:
        apartment_entire_stay -= apartment_entire_stay * .1

print(f"Apartment: {apartment_entire_stay:.2f} lv.")
print(f"Studio: {studio_entire_stay:.2f} lv.")
