read_age = float(input())
gender = input()

polite_address = ""

if gender == "m":
    if read_age >= 16:
        polite_address = "Mr."
    elif read_age < 16:
        polite_address = "Master"
if gender == "f":
    if read_age >= 16:
        polite_address = "Ms."
    elif read_age < 16:
        polite_address = "Miss"

print(polite_address)