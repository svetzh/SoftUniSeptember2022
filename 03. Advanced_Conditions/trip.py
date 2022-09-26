budget = float(input())
season = input()

price = 0
destination = ""
place = ""

if budget <= 100 and season == "summer":
    destination = "Bulgaria"
    budget = budget * .3
    place = "Camp"
elif budget <= 100 and season == "winter":
    destination = "Bulgaria"
    budget = budget * .7
    place = "Hotel"
elif budget <= 1000 and season == "summer":
    destination = "Balkans"
    budget = budget * .4
    place = "Camp"
elif budget <= 1000 and season == "winter":
    destination = "Balkans"
    budget = budget * .8
    place = "Hotel"
elif budget > 1000 and (season == "summer" or season == "winter"):
    destination = "Europe"
    budget = budget * .9
    place = "Hotel"

if destination == "Bulgaria":
    print(f"Somewhere in {destination}")
    print(f"{place} - {abs(budget):.2f}")
elif destination == "Balkans":
    print(f"Somewhere in {destination}")
    print(f"{place} - {abs(budget):.2f}")
elif destination == "Europe":
    print(f"Somewhere in {destination}")
    print(f"{place} - {abs(budget):.2f}")



