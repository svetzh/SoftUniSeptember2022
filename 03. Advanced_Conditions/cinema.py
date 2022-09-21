type_projection = input()
rows = int(input())
columns = int(input())

premiere = float(12.00)
normal_prod = float(7.50)
discount_prod = float(5.00)
income = 0
cinema_capacity = rows * columns

if type_projection == "Premiere":
    income = cinema_capacity * premiere
elif type_projection == "Normal":
    income = cinema_capacity * normal_prod
elif type_projection == "Discount":
    income = cinema_capacity * discount_prod

print(f"{income:.2f} leva")